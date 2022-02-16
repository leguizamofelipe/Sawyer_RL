from sawyer_env import *
import math
import gym
'''
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import make_vec_env
from stable_baselines import PPO2
'''

env = ArmMotionEnvironment()

ep_reward_list = []

# model = PPO2(MlpPolicy, env, verbose=1)
# model.learn(total_timesteps=10000)

for episode in range(400):
    ep_reward = 0
    observation = env.reset()
    for step in range(80):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # print(done)
        ep_reward += reward
    ep_reward_list.append(ep_reward)

for count, eprwd in enumerate(ep_reward_list): print(f'Episode {count} Reward: {eprwd}')

print('done')