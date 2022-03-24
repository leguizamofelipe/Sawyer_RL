from sawyer_dh_dqn_env import *

# from stable_baselines.common.policies import MlpPolicy
from stable_baselines3 import PPO
# from stable_baselines3.common import make_vec_env

env = DQNArmMotionEnvironment()

# env = make_vec_env(env, n_envs=4)

model = PPO('MlpPolicy', env, verbose = 1, device = 'cuda:1', learning_rate=0.01)

log_dir = 'logs/'

time_steps = 10e6

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

# results_plotter.plot_results([log_dir], time_steps, results_plotter.X_TIMESTEPS, "SawyerRL")
print('done?')