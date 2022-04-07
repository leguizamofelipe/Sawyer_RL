from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import SAC

target_dict = { 0: Point(0.602,0.681,0.317)}

env = ContinuousArmMotionEnvironment(target_dict)

time_steps = 500000

model = SAC('MlpPolicy', env, verbose = 1, device = 'cuda')

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

print('done?')