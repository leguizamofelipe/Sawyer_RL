from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import PPO

target_dict = {0: Point(0.602,0.681,0.317)}

env = ContinuousArmMotionEnvironment(target_dict=target_dict)

time_steps = 50000

for learning_rate in [0.001, 0.005, 0.01, 0.05]:
    model = PPO('MlpPolicy', env, verbose = 1, device = 'cuda:1', learning_rate=learning_rate)

    model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

    env.plot_rewards(added_title = learning_rate)

print('done?')