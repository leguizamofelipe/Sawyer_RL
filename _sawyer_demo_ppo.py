from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import PPO

'''
target_dict = { 0: Point(0.7315905137589676, 0.7115280197260334, 0.15348379395482878),
                1: Point(0.7801117441176564, 0.5500329764864156, 0.1842536897312016 ),
                2: Point(0.685123322687442,  0.6840350631055033, 0.47147110493178634)}

0.623157215	0.377598079	0.330619956
0.339878021	0.503960918	0.448421076
0.23093616	0.345445747	0.771748866
0.525180116	0.634260662	0.365209697
0.500952516	0.611139185	0.587357806
'''
target_dict = { 0: Point(0.602,0.681,0.317)}

# target_dict = { 0: Point(0.385,0.098,0.060)}

if len(target_dict) == 1:
    env_id = f'PPO-{target_dict[0].x}-{target_dict[0].y}-{target_dict[0].z}-{int(time.time())}'

env = ContinuousArmMotionEnvironment(target_dict=target_dict, env_id=env_id)

time_steps = 250000

model = PPO('MlpPolicy', env, verbose = 1, device = 'cuda:1')

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

model.save(os.path.join('logs', env_id, f'model_after{time_steps}'))

print('done?')