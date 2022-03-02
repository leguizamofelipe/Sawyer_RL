import itertools
import gym
from gym import spaces
import numpy as np
import random
from sawyer import *
from sawyer_dqn_env import *

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

env = DQNArmMotionEnvironment()

model  = PPO2(MlpPolicy, env, verbose = 1)
model.learn(total_timesteps=25000)

