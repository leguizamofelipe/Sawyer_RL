from sawyer import *
from sawyer_dqn_env import *
from callback import SaveOnBestTrainingRewardCallback
from stable_baselines import results_plotter
from stable_baselines.bench import Monitor

# from stable_baselines.common.policies import MlpPolicy
from stable_baselines3 import PPO

env = DQNArmMotionEnvironment()

model = PPO('MlpPolicy', env, verbose = 1)

log_dir = 'Sawyer_RL/logs/'
# env = Monitor(env, log_dir)

# callback = SaveOnBestTrainingRewardCallback(check_freq=500, log_dir = log_dir)

time_steps = 10e6

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

# results_plotter.plot_results([log_dir], time_steps, results_plotter.X_TIMESTEPS, "SawyerRL")
print('done?')