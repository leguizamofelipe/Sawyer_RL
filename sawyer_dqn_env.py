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

class DQNArmMotionEnvironment(gym.Env):
    """A robot arm motion environment for OpenAI gym"""
    metadata = {'render.modes': ['human']} # TODO understand what this does

    def __init__(self):
        super(DQNArmMotionEnvironment, self).__init__()
        # TODO Initialize Sawyer
        # self.S = Sawyer()

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
        '''
        Action space in DQN env should be continous

        self.joint_positions = {
            0 : np.arange(self.joint_maxes[0][0], self.joint_maxes[0][1]  + self.m_f , self.m_f ),
            1 : np.arange(self.joint_maxes[1][0], self.joint_maxes[1][1]  + self.m_f , self.m_f ),
            3 : np.arange(self.joint_maxes[3][0], self.joint_maxes[3][1]  + self.m_f , self.m_f ),
            5 : np.arange(self.joint_maxes[5][0], self.joint_maxes[5][1]  + self.m_f , self.m_f ),
        }
        '''
        self.reward_range = (0, 5000)

        # Actions: move any of the active joints joints in a +/- movement factor direction
        self.action_space = spaces.Box(low=np.ones(len(self.active_joints)), high=2*np.ones(len(self.active_joints)), dtype=int)

        # Set number of actions (number of joints to move)
        self.action_space.n = len(self.active_joints)

        # Observations: position of joints, mapped to the full range of a joint
        self.observation_space = spaces.Box(low = np.zeros(7), high=np.ones(7)) #spaces.Box(low = np.zeros(1), high = np.array([20]), dtype = float)

        # TODO Initialize target position (random Cartesian coordinate from 0-5 in x/y/z)
        # self.target_pos = self.S.Point(randrange(5),randrange(5),randrange(5))
        # print(f'* Targeting {self.target_pos}')

    def _take_action(self, action):
        # Do a bit of transformation to get correct matrix for robot motion
        # angles_array = self.find_target_angles(action)

        # self.S.move_to_angles(angles_array, printout=False)
        
        # state_array = []

        # for index, val in enumerate(angles_array):
        #     if index in self.active_joints:
        #         state_array.append(val)

        # state_array = np.around(np.array(state_array),1)

        # self.current_state = self.states_dict_inv[state_array.tobytes()]
        pass

    def valid_pose(self, target_angles):
        valid_pose = True

        for count, angle in enumerate(target_angles):
            if count in self.joint_positions.keys():
                if angle > self.joint_maxes[count][1] or angle < self.joint_maxes[count][0]:
                    valid_pose = False

        return valid_pose

    def step(self, action):
        # Case where we command robot to exceed its joint ranges. Establish high penalty
        '''
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
        '''

        self._take_action(action)

        obs = self._next_observation()

        reward = 1

        done = False 

        return obs, reward, done

    def _next_observation(self):
        # return self.S.angles
        return np.random.rand(7)

    def reset(self):
        # Reset the state of the environment to an initial state
        self.init_pose = np.zeros(7)

        # self.current_state_angles = self.init_pose
        
        # self.S.move_to_angles(self.current_state_angles, printout=False)

        # self.target_pos = self.S.Point(randrange(5),randrange(5),randrange(5))
        # print(f'* Targeting {self.target_pos}')

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
