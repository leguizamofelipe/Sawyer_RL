from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import SAC
from stable_baselines3.common.callbacks import EvalCallback

'''
target_dict_list = [
    {0: Point(0.707, 0.712,	0.719)},
    {0: Point(0.683, 0.722,	0.530)},
    {0: Point(0.590, 0.734,	0.630)},
    {0: Point(0.533, 0.792,	0.719)},
    {0: Point(0.766, 0.525,	0.781)},
]
'''
target_dict_list = [
    {0: Point(0.683,	0.722,	0.530)},
    {0: Point(0.712,	0.558,	0.650)},
    {0: Point(0.590,	0.734,	0.630)},
    # {0: Point(0.533,	0.682,	0.719)},
    # {0: Point(0.515,	0.525,	0.721)},
]

for target_dict in target_dict_list: 
  # for ent_coef in [0.1, 0.3, 0.5]:
    start=time.time()

    time_steps = 250000

    if len(target_dict) ==1:
        env_id = f'SAC-{target_dict[0].x}-{target_dict[0].y}-{target_dict[0].z}-{int(time.time())}'

    env = ContinuousArmMotionEnvironment(target_dict=target_dict, env_id=env_id)

    eval_callback = EvalCallback(env, best_model_save_path=f'./best_model-{env_id}/',
                                log_path=f'./best_model-{env_id}/', eval_freq=500,
                                deterministic=True, render=False)

    model = SAC('MlpPolicy', env, verbose = 1, device = 'cuda')

    model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30, callback=eval_callback)

    model.save(os.path.join('logs', env_id, f'model_after{time_steps}'))

    end = time.time()

    print(f'Runtime = {end-start}')
    os.makedirs(os.path.join('logs', env_id, f'Runtime_was_{end-start}'))