from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import SAC

# target_dict = { 0: Point(0.7315905137589676, 0.7115280197260334, 0.15348379395482878),
#                 1: Point(0.7801117441176564, 0.5500329764864156, 0.1842536897312016 ),
#                 2: Point(0.685123322687442,  0.6840350631055033, 0.47147110493178634)}

# target_dict = { 0: Point(0.602,0.681,0.317)}

# target_dict = { 0: Point(0.385,0.098,0.060)}

# target_dict = { 0: Point(0.517,0.693,0.254)}


'''
0.754187979	0.639408272	0.824093325
0.467220887	0.057780057	0.787238109
0.13345194	0.875891828	0.086447033
0.510392372	0.347903542	0.721052256
0.544116632	0.823207031	0.545415948
'''

# for learning_rate in 1/10*np.array([0.001, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01]):
env = ContinuousArmMotionEnvironment(target_dict=target_dict)

time_steps = 10e6

model = SAC('MlpPolicy', env, verbose = 1, device = 'cuda')

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

# env.plot_rewards(added_title = "")

print('done?')