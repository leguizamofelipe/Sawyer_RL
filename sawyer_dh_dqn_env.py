import gym
from gym import spaces
import numpy as np
import random
from dh_sawyer import *
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from random import randint

from episode_history import EpisodeHistory

class DQNArmMotionEnvironment(gym.Env):
    """A robot arm motion environment for OpenAI gym"""
    metadata = {'render.modes': ['human']} # TODO understand what this does

    def __init__(self, save_to_disk=False):
        super(DQNArmMotionEnvironment, self).__init__()

        # Initialize Sawyer
        self.S = DH_Sawyer()

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

        self.m_f = 0.01 # Was 0.02
        self.max_mf = 0.02

        # Actions: move any of the active joints joints in a +/- movement factor direction
        # self.action_space = spaces.Box(low=np.ones(len(self.active_joints)), high=2*np.ones(len(self.active_joints)), dtype=int)
        self.action_space = spaces.Box(low = -1 * np.ones(len(self.active_joints)), high = np.ones(len(self.active_joints)))
        
        # For discrete action space. Deprecated for now
        # actions_list = list(itertools.product([-1,1], repeat=len(self.active_joints)))
        # self.actions_dict = {count: np.array(action) for count, action in enumerate(actions_list)}
        # Set number of actions (number of joints to move)
        # self.action_space.n = len(self.active_joints)

        # TODO make this dynamically update depending on # of joints
        low  = np.array([0, 0, 0, 0, 0, 0, 0])
        high = np.array([1, 1, 1, 1, 1.5, 1.5, 1.5])

        # Observations: position of joints, mapped to the full range of a joint. Last three vals in array are position
        self.observation_space = spaces.Box(low = low, high=high) #spaces.Box(low = np.zeros(1), high = np.array([20]), dtype = float)
        # self.observation_space.n = 
        # self.action_count = 0
        self.hist = None
        self.hist_list = []

        self.save_to_disk = save_to_disk

        # self.fig = plt.figure()

        num_targets = 1
        self.target_dict = {}

        for i in range(0, num_targets):
            self.target_dict.update({i: self.S.Point(random.uniform(0.5,0.8),random.uniform(0.5,0.8),random.uniform(0,0.8))})

        # self.target_pos = self.S.Point(random.uniform(0.5,1),random.uniform(0.5,1),random.uniform(0,1))
        self.target_pos = self.target_dict[randint(0,num_targets-1)]

    def _action_to_angles(self, action):
        # Action space is moving joints +/- movement factor (+ is 2, - is 1)
        # Need to map to appropriate motion

        joint_angles = self.S.angles.copy()

        for count, joint in enumerate(self.active_joints):
            joint_angles[joint] += self.max_mf * action[count]

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

            # Objective component - discourage being far away from target
            reward = -50*(self.S.distance_from_target(self.target_pos)**2)
            # reward = 0
            # Marginal component - encourage making steps in the right direction
            # reward += 1000 * (self.prev_dist - self.S.distance_from_target(self.target_pos))

            obs = self._next_observation()

            self.prev_dist = self.S.distance_from_target(self.target_pos)

            done = False
            
            if self.S.distance_from_target(self.target_pos) < 0.1:
                reward = 200
                done = True

            if self.action_count > 100:
                reward = -20
                done = True

        self.hist.record_endpoint(self.S.endpoint)
        self.hist.record_reward(reward)

        return obs, reward, done, {}

    def _next_observation(self):
        e = self.S.endpoint
        obs = np.zeros(len(self.active_joints) + 3)

        i = 0
        for joint, angle in enumerate(self.S.angles):
            if joint in self.active_joints:
                obs[i] = self.S.angles[joint]
                i+=1

        # obs[0:len(self.active_joints)] = np.array(self.S.angles)
        obs[len(self.active_joints):10] = np.array([e.x, e.y, e.z])

        return obs

    def reset(self):
        # Reset the state of the environment to an initial state
        prev_endpoint = self.S.endpoint
        self.action_count = 0

        init_angles = np.array([0.75, 0, 0, 0, 0, 0, 0])

        self.S.move_to_angles(init_angles, printout=False)
        self.S.sleep(0.2)

        self.init_pos = self.S.endpoint

        self.prev_dist = self.S.distance_from_target(self.target_pos)
        
        if self.hist is not None:
            self.hist_list.append(self.hist)
            
            if self.save_to_disk:
                self._reward_df = pd.concat([self._reward_df, pd.DataFrame([[self.hist.total_reward(), self.hist.start_time, f'X {self.target_pos.x} Y {self.target_pos.y} Z {self.target_pos.z}', f'X {prev_endpoint.x} Y {prev_endpoint.y} Z {prev_endpoint.z}']], columns = ['Reward', 'Time Started', 'Target Pos', 'Ending Pos'])])
                # plt.scatter(len(self.hist_list), self.hist.total_reward(), c = 'blue')
                # plt.show()
                self._reward_df.reset_index().to_csv('logs/reward.csv')
        else:
            self._reward_df = pd.DataFrame(columns = ['Reward', 'Time Started'])

        # reward_df = pd.DataFrame([f'{episode.total_reward()}, {episode.start_time}' for episode in self.hist_list])

        self.hist = EpisodeHistory(0, self.init_pos, self.target_pos)

        return self._next_observation()

    def plot_rewards(self):
        reward_list = [x.total_reward() for x in self.hist_list]
        plt.plot(reward_list)
        plt.title(f'Rewards vs time for {len(reward_list)} episodes')
        plt.xlabel('Episode')
        plt.ylabel('Reward')

        x = range(reward_list)
        y = reward_list

        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x,p(x),"r--")

        plt.tight_layout()
        plt.show()
