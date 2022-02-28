import math
import itertools
import gym
from gym import spaces
import numpy as np
import random

class DQNArmMotionEnvironment(gym.Env):
    """A robot arm motion environment for OpenAI gym"""
    metadata = {'render.modes': ['human']} # TODO understand what this does

    def __init__(self):
        super(DQNArmMotionEnvironment, self).__init__()
        # Initialize Sawyer
        self.S = Sawyer()

        # Define which joints are used
        self.active_joints = {   
                            0 : {'Max': 1.5, 'Min': 0}, 
                            1 : {'Max': 1, 'Min': -1}, 
                            #'2', 
                            3 : {'Max': 2, 'Min': -2}, 
                            #'4', 
                            5 : {'Max': 2, 'Min': -2}, 
                            #'6'
        }

        self.m_f = 0.02

        # Actions: move any of the active joints joints in a +/- movement factor direction
        # self.action_space = spaces.Box(low=np.ones(len(self.active_joints)), high=2*np.ones(len(self.active_joints)), dtype=int)
        self.action_space = spaces.Discrete(16)

        actions_list = list(itertools.product([-1,1], repeat=len(self.active_joints)))

        self.actions_dict = {count: np.array(action) for count, action in enumerate(actions_list)}

        # Set number of actions (number of joints to move)
        self.action_space.n = len(self.active_joints)

        # Observations: position of joints, mapped to the full range of a joint
        self.observation_space = spaces.Box(low = np.zeros(7), high=np.ones(7)) #spaces.Box(low = np.zeros(1), high = np.array([20]), dtype = float)

        self.observation_space.n = 7
    def _action_to_angles(self, action):
        # Action space is moving joints +/- movement factor (+ is 2, - is 1)
        # Need to map to appropriate motion

        joint_angles = self.S.angles.copy()

        active_count = 0
        for joint, angle in enumerate(joint_angles):
            if joint in self.active_joints:
                joint_angles[joint] += self.m_f * self.actions_dict[action][active_count]
                active_count += 1

        return joint_angles

    def _take_action(self, action):
        angles = self._action_to_angles(action)
        self.S.move_to_angles(angles, printout=False)
        pass

    def valid_pose(self, target_angles):
        valid_pose = True

        for joint, angle in enumerate(target_angles):
            if joint in self.active_joints:
                if angle > self.active_joints[joint]['Max'] or angle < self.active_joints[joint]['Min']:
                    valid_pose = False

        return valid_pose

    def step(self, action):
        # Case where we command robot to exceed its joint ranges. Establish high penalty
        if not self.valid_pose(self._action_to_angles(action)):
            reward = -5
            obs = self._next_observation()
            done = self.S.distance_from_target(self.target_pos) < 0.01
            self.prev_dist = self.S.distance_from_target(self.target_pos)
            return obs, reward, done
        else:
            # Set the current robot position
            self._take_action(action)

            # self.S.sleep(0.25)

            # Calculate reward
            if self.S.distance_from_target(self.target_pos) < self.prev_dist:
                reward = 1
            else:
                reward = 0

            done = self.S.distance_from_target(self.target_pos) < 0.25

            obs = self._next_observation()

            self.prev_dist = self.S.distance_from_target(self.target_pos)

        return obs, reward, done

    def _next_observation(self):
        return np.array(self.S.angles)

    def reset(self):
        # Reset the state of the environment to an initial state
        init_pose = np.array([0.75, 0, 0, 0, 0, 0, 0])

        self.S.move_to_angles(init_pose, printout=False)

        self.target_pos = self.S.Point(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))

        self.prev_dist = self.S.distance_from_target(self.target_pos)

        return self._next_observation()

# Python Representation of Sawyer robot
class Sawyer():
    def __init__(self):
        from rospy import sleep
        import rospy
        import intera_interface

        # initialize our ROS node, registering it with the Master
        rospy.init_node('Hello_Sawyer')

        # create an instance of intera_interface's Limb class
        self.limb = intera_interface.Limb('right')

        # TODO: Find a way to make this update and easily callable in the form S.angles()
        # Not sure how it interfaces with rostopics, leave for now
        # get the right limb's current joint angles
        self.angles = list(self.limb.joint_angles().values())

        # initialize endpoint position
        self.endpoint = self.limb.endpoint_pose()['position']

        # print the current joint angles
        print("* Initialized at {}".format(str(self.angles)))
	
    class Point():
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        def __repr__(self):
            return str(f'{self.x},{self.y},{self.z}')

    def sleep(self, time):
        import rospy
        rospy.sleep(time)
        
    def move_to_angles(self, angular_array, printout = True):
        angles = {  'right_j0': angular_array[0], 
                    'right_j1': angular_array[1], 
                    'right_j2': angular_array[2],
                    'right_j3': angular_array[3], 
                    'right_j4': angular_array[4], 
                    'right_j5': angular_array[5],
                    'right_j6': angular_array[6],
        }
        if printout: print("* Commanding move to {}\n".format(str(angular_array)))
        self.limb.move_to_joint_positions(angles)
        self.angles = list(self.limb.joint_angles().values())
        self.endpoint = self.limb.endpoint_pose()['position']
        if printout: print("* Completed move to {}\n".format(str(self.angles)))

    def distance_from_target(self, target):
        # Current position
        c = self.endpoint

        # Target position
        t = target

        distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
        
        return distance
