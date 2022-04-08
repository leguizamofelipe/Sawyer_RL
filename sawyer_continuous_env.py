import gym
from gym import spaces
import numpy as np
import random

from sawyer import *
import pandas as pd
import os

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time

import pickle

from random import randint

from episode_history import EpisodeHistory

class ContinuousArmMotionEnvironment(gym.Env):
    """A robot arm motion environment for OpenAI gym"""
    metadata = {'render.modes': ['human']} # TODO understand what this does

    def __init__(self, save_to_disk=False, target_dict = None, env_id = int(time.time()), sim_type = 'DH'):
        super(ContinuousArmMotionEnvironment, self).__init__()

        # Initialize Sawyer
        self.S = Sawyer(mode =  sim_type)

        self.sim_type = sim_type

        self.env_id = env_id

        self.save_dir = os.path.join('logs', str(env_id))
        os.makedirs(self.save_dir)
        
        # Define which joints are used
        self.active_joints = {   
            0 : {'Max': 1.5, 'Min': 0}, 
            1 : {'Max': 1, 'Min': -1}, 
            2 : {'Max': 3, 'Min': -3},  
            3 : {'Max': 2, 'Min': -2}, 
            4 : {'Max': 2, 'Min': -2}, 
            5 : {'Max': 2, 'Min': -2}, 
            6 : {'Max': 2, 'Min': -2}, 
        }

        self.box = {
            'x' : {'Min': 0.5, 'Max': 0.8}, 
            'y' : {'Min': 0.5, 'Max': 0.8}, 
            'z' : {'Min': 0.5, 'Max': 0.8},  
        }

        self.m_f = 0.01 # Was 0.02
        self.max_mf = 0.02

        # Actions: move any of the active joints joints in a +/- movement factor direction
        # self.action_space = spaces.Box(low=np.ones(len(self.active_joints)), high=2*np.ones(len(self.active_joints)), dtype=int)
        self.action_space = spaces.Box(low = -1 * np.ones(len(self.active_joints)), high = np.ones(len(self.active_joints)), dtype=np.float32)
        self.action_space.n = len(self.active_joints)

        # TODO make this dynamically update depending on # of joints
        cartesian_pose_low = np.array([-1, -1, -1])
        cartesian_pose_high = np.array([1, 1, 1])
        joint_angles_low = np.array([-1]*len(self.active_joints))
        joint_angles_high = np.array([1]*len(self.active_joints))

        self.observation_space = spaces.Box
        self.observation_space.low  = np.concatenate((joint_angles_low, cartesian_pose_low))
        self.observation_space.high = np.concatenate((joint_angles_high, cartesian_pose_high))

        # Observations: position of joints, mapped to the full range of a joint. Last three vals in array are position
        self.observation_space = spaces.Box(low = self.observation_space.low, high=self.observation_space.high, dtype=np.float32) 
        self.observation_space.n = len(self.observation_space.low)
        # self.action_count = 0
        self.hist = None
        self.hist_list = []

        self.ep_count = 0

        self.save_to_disk = save_to_disk

        self.target_dict = {}

        if target_dict is None:
            self.num_targets = 5
            for i in range(0, self.num_targets):
                self.target_dict.update({i: Point(random.uniform(self.box['x']['Min'],self.box['x']['Max']),random.uniform(self.box['y']['Min'],self.box['y']['Max']),random.uniform(self.box['z']['Min'],self.box['z']['Max']))})
        else:
            self.target_dict = target_dict
            self.num_targets = len(target_dict)

        # self.target_pos = self.S.Point(random.uniform(0.5,1),random.uniform(0.5,1),random.uniform(0,1))
        self.target_pos = self.target_dict[randint(0,self.num_targets-1)]

    def _action_to_angles(self, action):
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
        target_tolerance = 0.01
        # Case where we command robot to exceed its joint ranges. Establish high penalty
        self.action_count += 1
        if not self.valid_pose(self._action_to_angles(action)):
            reward = -5
            obs = self._next_observation()
            done = self.S.distance_from_target(self.target_pos) < target_tolerance or self.action_count == 50
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
            
            if self.S.distance_from_target(self.target_pos) < target_tolerance:
                reward = 200
                done = True

            if self.action_count > 100:
                reward = -20
                done = True

        self.hist.record_endpoint(self.S.endpoint)
        self.hist.record_reward(reward)

        return obs, reward, done, {}

    def _next_observation(self):
        e = self.target_pos

        obs = np.zeros(len(self.active_joints) + 3)

        i = 0
        for joint, angle in enumerate(self.S.angles):
            if joint in self.active_joints:
                ang_normalized = self.norm(angle, self.active_joints[joint]['Max'], self.active_joints[joint]['Min']) 
                obs[i] = ang_normalized
                i+=1

        obs[len(self.active_joints):10] = np.array([self.norm(e.x, self.box['x']['Max'], self.box['x']['Min']), 
                                                    self.norm(e.y, self.box['y']['Max'], self.box['y']['Min']),
                                                    self.norm(e.z, self.box['z']['Max'], self.box['z']['Min'])])

        return obs

    def norm(self, x, x_max, x_min):
        return 2 * (x-x_min)/(x_max-x_min) - 1

    def denorm(self, x_norm, x_max, x_min):
        return (x_norm + x_max - x_min)/2 + x_min 

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

        self.target_pos = self.target_dict[randint(0,self.num_targets-1)]

        self.hist = EpisodeHistory(0, self.init_pos, self.target_pos)

        self.ep_count +=1

        # Save every 500 intervals
        save_interval = 500
        if self.ep_count % save_interval == 0:
            if self.sim_type == 'Gazebo':
                pickle.dump(self.hist_list, open(os.path.join(self.save_dir, "env_hist_list_autosave.p"), "wb" ))
            else:
                pickle.dump(self, open(os.path.join(self.save_dir, "env_autosave.p"), "wb" ))

        return self._next_observation()

    def plot_rewards(self, added_title):
        reward_list = [x.total_reward() for x in self.hist_list]
        plt.plot(reward_list)
        plt.title(f'Rewards vs time for {len(reward_list)} episodes')
        plt.xlabel('Episode')
        plt.ylabel('Reward')

        plt.tight_layout()
