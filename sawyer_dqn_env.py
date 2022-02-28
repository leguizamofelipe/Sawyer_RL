import math
import itertools
import gym
from gym import spaces
import numpy as np
import random
from sawyer import *

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class EpisodeHistory():
    def __init__(self, ep_no, init, target) -> None:
        self.ep_no = ep_no
        self.endpoint_history = []
        self.reward_history = []
        self.cumulative_reward_history = []
        self.first_timestep = True
        self.target = target
        self.init = init
    def record_endpoint(self, endpoint):
        self.endpoint_history.append(endpoint)
    def record_reward(self, reward):
        self.reward_history.append(reward)
        if self.first_timestep:
            self.prev_reward = 0
            self.first_timestep = False
        else:
            self.prev_reward = self.cumulative_reward_history[-1]
        self.cumulative_reward_history.append(reward + self.prev_reward)
    def total_reward(self):
        return sum(self.reward_history)
    def record_steps(self, steps):
        self.final_steps = steps
    def plot_episode_3D(self):
        ax = plt.axes(projection = '3d')
        ax.set_xlim([0.5,1])
        ax.set_ylim([0.5,1])
        ax.set_zlim([0,1])
        x_list = [point.x for point in self.endpoint_history]
        y_list = [point.y for point in self.endpoint_history]
        z_list = [point.z for point in self.endpoint_history]
        ax.plot3D(x_list, y_list, z_list, 'blue')
        ax.scatter3D(self.init.x, self.init.y, self.init.z, color = 'r')
        ax.scatter3D(self.target.x, self.target.y, self.target.z, color = 'g')
        ax.set_title(f'n_steps: {len(self.endpoint_history)} | reward: {self.cumulative_reward_history[-1]}')
        plt.tight_layout()

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

            done = self.S.distance_from_target(self.target_pos) < 0.1

            obs = self._next_observation()

            self.prev_dist = self.S.distance_from_target(self.target_pos)

        return obs, reward, done

    def _next_observation(self):
        return np.array(self.S.angles)

    def reset(self):
        # Reset the state of the environment to an initial state
        init_angles = np.array([0.75, 0, 0, 0, 0, 0, 0])

        self.S.move_to_angles(init_angles, printout=False)
        self.S.sleep(0.2)

        self.init_pos = self.S.endpoint

        self.target_pos = self.S.Point(random.uniform(0.5,1),random.uniform(0.5,1),random.uniform(0,1))

        self.prev_dist = self.S.distance_from_target(self.target_pos)

        return self._next_observation()
