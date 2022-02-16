import math
import gym
from gym import spaces
import numpy as np
from gym import spaces
import numpy as np
import torch
import pfrl

from rospy import sleep
import rospy
import intera_interface

from random import randrange

from intera_interface.limb import Point

class SawyerEnv():

    '''
    Description:

    Robotic arm with seven joint angles.
    Range of motion for each: 

    Observation:
        #TODO: Include current state of joints, and inst. vel? in obs space
        Type: float
        Num     Observation               Min                     Max
        0       Distance from target      0                       5000 (infinity)
    
    Actions:
        #TODO: Could restrict motion to subset of joints
        Type: Discrete(2)
        Num   Action
        0     Increase joint 0 pose by +set movement factor
        1     Increase joint 0 pose by -set movement factor
        2     Increase joint 1 pose by +set movement factor
        3     Increase joint 1 pose by -set movement factor
        4     Increase joint 2 pose by +set movement factor
        5     Increase joint 2 pose by -set movement factor
        6     Increase joint 3 pose by +set movement factor
        7     Increase joint 3 pose by -set movement factor
        8     Increase joint 4 pose by +set movement factor
        9     Increase joint 4 pose by -set movement factor
        10    Increase joint 5 pose by +set movement factor
        11    Increase joint 5 pose by -set movement factor
        12    Increase joint 6 pose by +set movement factor
        13    Increase joint 6 pose by -set movement factor

    Reward:
        +1 for every step taken where distance is less than previous distance
        TODO: Function of magnitude of distance delta: getting much closer = higher reward

    Episode Termination:

    '''

class ArmMotionEnvironment(gym.Env):
    """A robot arm motion environment for OpenAI gym"""
    metadata = {'render.modes': ['human']} # TODO understand what this does

    def __init__(self):
        # Initialize Sawyer
        super(ArmMotionEnvironment, self).__init__()
        self.S = Sawyer()

        # Initialize target position (random Cartesian coordinate from 0-5 in x/y/z)
        self.target_pos = self.S.Point(randrange(5),randrange(5),randrange(5))
        print(f'* Targeting {self.target_pos}')
        self.prev_dist = self.S.distance_from_target(self.target_pos)

        self.reward_range = (0, 5000)
        m_f = 0.1

        # Actions: move any of the 7 joints in a +/- movement factor direction
        self.action_space = spaces.Box(low=-m_f*np.ones(7), high=m_f*np.ones(7), dtype=float)
        
        # Observations: distance from target; set min 0, max 20 (infinite)
        self.observation_space = spaces.Box(low = np.zeros(1), high = np.array([20]), dtype = float)

        # Initialize P matrix
        num_actions = 49
        self.P = {
            state: {action: [] for action in range(num_actions)}
            for state in range(num_states)
        }

        # Initialize Q function
        class QFunction(torch.nn.Module):
            def __init__(self, obs_size, n_actions):
                super().__init__()
                self.l1 = torch.nn.Linear(obs_size, 50)
                self.l2 = torch.nn.Linear(50, 50)
                self.l3 = torch.nn.Linear(50, n_actions)

            def forward(self, x):
                h = x
                h = torch.nn.functional.relu(self.l1(h))
                h = torch.nn.functional.relu(self.l2(h))
                h = self.l3(h)
                return pfrl.action_value.DiscreteActionValue(h)

        obs_size = self.observation_space.low.size
        # n_actions = self.action_spac
        # q_func = QFunction(obs_size, n_actions)


    def _take_action(self, action):
        action_array = action

        self.S.move_to_angles(action_array, printout=False)

    def step(self, action):
        # Set the current robot position randomly
        self._take_action(action)

        # Calculate reward

        if self.S.distance_from_target(self.target_pos) < self.prev_dist:
            reward = 1
        else:
            reward = 0

        done = self.S.distance_from_target(self.target_pos) < 0.25

        obs = self._next_observation()

        self.prev_dist = self.S.distance_from_target(self.target_pos)

        return obs, reward, done, {}

    def _next_observation(self):
        return self.S.angles

    def reset(self):
        # Reset the state of the environment to an initial state (ie all joints at zero)
        self.angles = np.zeros(7)
        self.S.move_to_angles(self.angles, printout=False)

        self.target_pos = self.S.Point(randrange(5),randrange(5),randrange(5))
        print(f'* Targeting {self.target_pos}')

        return self._next_observation()

# Python Representation of Sawyer robot
class Sawyer():
    def __init__(self):
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
