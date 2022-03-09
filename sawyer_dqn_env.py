import math
import itertools
import gym
from gym import spaces
import numpy as np
import random
from sawyer import *
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from episode_history import EpisodeHistory

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
        self.action_count = 0
        self.hist = None
        self.hist_list = []

        self.fig = plt.figure()

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
        self.action_count += 1
        if not self.valid_pose(self._action_to_angles(action)):
            reward = -5
            obs = self._next_observation()
            done = self.S.distance_from_target(self.target_pos) < 0.01 or self.action_count == 50
            self.prev_dist = self.S.distance_from_target(self.target_pos)
            return obs, reward, done, {}
        else:
            # Set the current robot position
            self._take_action(action)

            # Calculate reward
            if self.S.distance_from_target(self.target_pos) < self.prev_dist:
                reward = 1
            else:
                reward = 0

            obs = self._next_observation()

            self.prev_dist = self.S.distance_from_target(self.target_pos)

            done = self.S.distance_from_target(self.target_pos) < 0.1 or self.action_count == 50

        self.hist.record_endpoint(self.S.endpoint)
        self.hist.record_reward(reward)

        return obs, reward, done, {}

    def _next_observation(self):
        return np.array(self.S.angles)

    def reset(self):
        # Reset the state of the environment to an initial state

        self.action_count = 0

        init_angles = np.array([0.75, 0, 0, 0, 0, 0, 0])

        self.S.move_to_angles(init_angles, printout=False)
        self.S.sleep(0.2)

        self.init_pos = self.S.endpoint

        self.target_pos = self.S.Point(random.uniform(0.5,1),random.uniform(0.5,1),random.uniform(0,1))

        self.prev_dist = self.S.distance_from_target(self.target_pos)
        
        if self.hist is not None:
            self.hist_list.append(self.hist)
            
            self._reward_df = pd.concat([self._reward_df, pd.DataFrame([[self.hist.total_reward(), self.hist.start_time]], columns = ['Reward', 'Time Started'])])
            # plt.scatter(len(self.hist_list), self.hist.total_reward(), c = 'blue')
            # plt.show()
            self._reward_df.reset_index().to_csv('Sawyer_RL/logs/reward.csv')
        else:
            self._reward_df = pd.DataFrame(columns = ['Reward', 'Time Started'])

        # reward_df = pd.DataFrame([f'{episode.total_reward()}, {episode.start_time}' for episode in self.hist_list])

        self.hist = EpisodeHistory(0, self.init_pos, self.target_pos)

        return self._next_observation()
