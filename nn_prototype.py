from sawyer_dqn_env import *

import pfrl
import torch
import torch.nn
import gym
import numpy

env = DQNArmMotionEnvironment()

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

obs_size = env.observation_space.low.size
n_actions = env.action_space.n
q_func = QFunction(obs_size, n_actions)

optimizer = torch.optim.Adam(q_func.parameters(), eps=1e-2)

gamma = 0.9

# What do these do?
explorer = pfrl.explorers.ConstantEpsilonGreedy(epsilon=0.3, random_action_func=env.action_space.sample)
replay_buffer = pfrl.replay_buffers.ReplayBuffer(capacity=10 ** 6)
phi = lambda x: x.astype(numpy.float32, copy=False)
gpu = -1

agent = pfrl.agents.DoubleDQN(
    q_func,
    optimizer,
    replay_buffer,
    gamma,
    explorer,
    replay_start_size=500,
    update_interval=1,
    target_update_interval=100,
    phi=phi,
    gpu=gpu,
)

n_episodes = 300
max_ep_len = 100
for episode in range(n_episodes):
    ep_state_history = []
    ep_reward = 0
    observation = env.reset()
    for step in range(80):
        action = agent.act(observation)
        # action = env.action_space.sample()
        observation, reward, done = env.step(action)

        reset = step == max_ep_len
        # print(done)
        agent.observe(observation, reward, done, reset)
        ep_reward += reward

    print(f"    *Done with episode {episode}, reward was {ep_reward}")


print('done')

'''
from sawyer_dqn_env import *
import gym
import pandas as pd
import numpy as np
# Neural network 
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
# Plotting
import matplotlib.pyplot as plt 
import seaborn as sns 

# Governing parameters for learning
alpha = 0.1
gamma = 0.6
epsilon = 0.1


env = DQNArmMotionEnvironment(alpha, gamma, epsilon)

n_actions = env.action_space.n  # dim of output layer 
input_dim = env.observation_space.shape[0]  # dim of input layer 
model = Sequential()
model.add(Dense(64, input_dim = input_dim , activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(n_actions, activation = 'linear'))
model.compile(optimizer=Adam(), loss = 'mse')

n_episodes = 1000
gamma = 0.99
epsilon = 1
minibatch_size = 32
cumulative_rewards = []
replay_memory = []
mem_max_size = 100000

for episode in range(n_episodes):
    ep_state_history = []
    ep_reward = 0
    observation = env.reset()
    for step in range(80):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # print(done)
        env.update_q(env.current_state, action)
        ep_reward += reward
        ep_state_history.append(env.current_state)

    print(f"    *Done with episode {episode}, reward was {ep_reward}")
    ep_reward_list.append(ep_reward)

for count, eprwd in enumerate(ep_reward_list): print(f'Episode {count} Reward: {eprwd}')
'''