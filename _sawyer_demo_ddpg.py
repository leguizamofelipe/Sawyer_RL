from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import DDPG
from stable_baselines3.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise

target_dict = {0: Point(0.602,0.681,0.317)}

# for learning_rate in np.array([0.001, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01]):
env = ContinuousArmMotionEnvironment(target_dict=target_dict)

time_steps = 10000

n_actions = env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))

model = DDPG('MlpPolicy', env, verbose = 1, device = 'cuda:1')

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

env.plot_rewards(added_title = learning_rate)

print('done?')