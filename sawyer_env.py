from csv import reader
import math
from sre_parse import State
import gym
from gym import spaces
import numpy as np
from gym import spaces
import numpy as np
import torch
import pfrl

import state_utilities
import itertools
import random
from random import randrange

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

    def __init__(self, alpha, gamma, epsilon):
        # Initialize Q learning parameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # Initialize Sawyer
        super(ArmMotionEnvironment, self).__init__()
        self.S = Sawyer()

        # Define which joints are used
        self.active_joints = [   
                            0, 
                            1, 
                            #'2', 
                            3, 
                            #'4', 
                            5, 
                            #'6'
                            ]

        self.m_f = 0.3

        self.joint_maxes = {
            0 : [ 0 , 1.5],
            1 : [-1 ,  1 ],
            3 : [-2 ,  2 ],
            5 : [-2 ,  2 ],
        }

        self.joint_positions = {
            0 : np.arange(self.joint_maxes[0][0], self.joint_maxes[0][1]  + self.m_f , self.m_f ),
            1 : np.arange(self.joint_maxes[1][0], self.joint_maxes[1][1]  + self.m_f , self.m_f ),
            3 : np.arange(self.joint_maxes[3][0], self.joint_maxes[3][1]  + self.m_f , self.m_f ),
            5 : np.arange(self.joint_maxes[5][0], self.joint_maxes[5][1]  + self.m_f , self.m_f ),
        }

        self.reward_range = (0, 5000)

        # Actions: move any of the active joints joints in a +/- movement factor direction
        self.action_space = spaces.Box(low=np.ones(len(self.active_joints)), high=2*np.ones(len(self.active_joints)), dtype=int)
        
        # Observations: distance from target; set min 0, max 20 (infinite)
        self.observation_space = spaces.Box(low = np.zeros(1), high = np.array([20]), dtype = float)

        # Initialize P matrix
        num_actions = len(self.active_joints)**2
        num_states, self.states_dict = state_utilities.find_num_states(self.m_f, self.joint_positions)

        actions_list = list(itertools.product([-1,1], repeat=len(self.active_joints)))

        self.actions_dict = {count: np.array(action) for count, action in enumerate(actions_list)}

        self.actions_dict_inv = {value.tobytes(): key for key, value in list(self.actions_dict.items())}

        '''
        Original definition of P: {state: {action: joint_positions}}

        self.P = {
            state: {count: action * self.m_f + self.states_dict[count] for count, action in enumerate(actions_matrix)}
            for state in range(num_states)
        }
        '''

        self.P = {
            state: {count: action * self.m_f + self.states_dict[count] for count, action in list(self.actions_dict.items())}
            for state in range(num_states)
        }        

        self.states_dict_inv = {value.tobytes(): key for key, value in list(self.states_dict.items())}        

        # Initialize Q function
        self.Q = {
            state: {count: 0 for count in range(len(self.actions_dict))}
            for state in range(num_states)
        }
        
        # Initialize target position (random Cartesian coordinate from 0-5 in x/y/z)
        self.target_pos = self.S.Point(randrange(5),randrange(5),randrange(5))
        print(f'* Targeting {self.target_pos}')

        # Move to init state
        init_state = random.randint(0, len(self.states_dict))
        
        init_targets = self.states_dict[init_state]
        init_pose = np.zeros(7)
        for count, active_joint in enumerate(self.active_joints):
            init_pose[active_joint] = init_targets[count]

        self.S.move_to_angles(init_pose)
        self.current_state = init_state
        self.current_state_angles = init_pose

        self.prev_dist = self.S.distance_from_target(self.target_pos)
    
    def update_q(self, state, action):
        action_filtered = action.copy()
        action_filtered[action==1] = -1
        action_filtered[action==2] = 1

        action = self.actions_dict_inv[action_filtered.tobytes()]

        current_q = self.Q[state][action]
        max_q = max(list(self.Q[0].values()))
        reward = self.current_reward

        # self, alpha, current_q, gamma, reward, max_q
        return (1-self.alpha) * current_q + self.alpha * (reward + self.gamma * max_q)

    def _take_action(self, action):
        # Do a bit of transformation to get correct matrix for robot motion
        angles_array = self.find_target_angles(action)

        self.S.move_to_angles(angles_array, printout=False)
        
        state_array = []

        for index, val in enumerate(angles_array):
            if index in self.active_joints:
                state_array.append(val)

        state_array = np.around(np.array(state_array),1)

        self.current_state = self.states_dict_inv[state_array.tobytes()]

    def find_target_angles(self, action):
        action_filtered = action.copy()
        angles_array = self.current_state_angles.copy()
        action_filtered[action==1] = -1
        action_filtered[action==2] = 1
        
        for count, active_joint in enumerate(self.active_joints):
            angles_array[active_joint] += action_filtered[count] * self.m_f

        return angles_array

    def valid_pose(self, target_angles):
        valid_pose = True

        for count, angle in enumerate(target_angles):
            if count in self.joint_positions.keys():
                if angle > self.joint_maxes[count][1] or angle < self.joint_maxes[count][0]:
                    valid_pose = False

        return valid_pose

    def step(self, action):
        # Case where we command robot to exceed its joint ranges. Establish high penalty
        if not self.valid_pose(self.find_target_angles(action)):
            reward = -5
            self.current_reward = reward
            obs = self._next_observation()
            done = self.S.distance_from_target(self.target_pos) < 0.25
            self.prev_dist = self.S.distance_from_target(self.target_pos)
            return obs, reward, done, {}
        
        # Set the current robot position
        self._take_action(action)

        # Calculate reward

        if self.S.distance_from_target(self.target_pos) < self.prev_dist:
            reward = 1
        else:
            reward = 0

        done = self.S.distance_from_target(self.target_pos) < 0.25

        obs = self._next_observation()

        self.current_reward = reward

        self.prev_dist = self.S.distance_from_target(self.target_pos)

        return obs, reward, done, {}

    def _next_observation(self):
        return self.S.angles

    def reset(self):
        # Reset the state of the environment to an initial state
        self.current_state = random.randint(0, len(self.states_dict))
        self.init_targets = self.states_dict[self.current_state]
        self.init_pose = np.zeros(7)

        for count, active_joint in enumerate(self.active_joints):
            self.init_pose[active_joint] = self.init_targets[count]

        self.current_state_angles = self.init_pose
        
        self.S.move_to_angles(self.current_state_angles, printout=False)

        self.target_pos = self.S.Point(randrange(5),randrange(5),randrange(5))
        print(f'* Targeting {self.target_pos}')

        return self._next_observation()

    # def ():

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
