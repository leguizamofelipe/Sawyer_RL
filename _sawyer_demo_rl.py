from sawyer_rl_env import *
import math
import gym
import matplotlib.pyplot as plt

# Governing parameters for learning
alpha = 0.1
gamma = 0.6
epsilon = 0.1

env = ArmMotionEnvironment(alpha, gamma, epsilon)

ep_reward_list = []

for episode in range(400):
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


