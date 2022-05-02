from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import PPO

import shutil

target_dict =     {0: Point(0.590,	0.734,	0.630),
                   0: Point(0.515,	0.525,	0.721),
                   0: Point(0.533,	0.682,	0.719),
                   0: Point(0.683,	0.722,	0.530),
                   0: Point(0.712,	0.558,	0.650),}

            
start=time.time()

time_steps = 1e6

if len(target_dict) ==1:
    env_id = f'PPO-DH-Multiple-Points-EucledianDist-{int(time.time())}'

env = ContinuousArmMotionEnvironment(sim_type = 'DH', save_to_disk = False, target_dict=target_dict, env_id=env_id)

model = PPO('MlpPolicy', env, verbose = 1, device = 'cuda')

model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

model.save(os.path.join('logs', env_id, f'model_after{model.num_timesteps}'))

end = time.time()

print(f'Runtime = {end-start}')
    
# shutil.copyfile('logs/reward.csv', os.path.join('logs', env_id, 'rewards.csv'))

os.makedirs(os.path.join('logs', env_id, f'Runtime_was_{end-start}'))
