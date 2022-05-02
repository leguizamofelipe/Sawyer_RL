from turtle import done
from torch import device
from sawyer_continuous_env import *
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback

import shutil

time_steps = 250000

target_dicts = [
    {0: Point(0.590,	0.734,	0.630)},
    {0: Point(0.515,	0.525,	0.721)},
    {0: Point(0.533,	0.682,	0.719)},
    {0: Point(0.683,	0.722,	0.530)},
    {0: Point(0.712,	0.558,	0.650)},
]

trained_agent = [

    'logs/PPO-Acc-0.59-0.734-0.63-1649885884/model_after250000.zip', 
    'logs/PPO-Acc-0.515-0.525-0.721-1649887136/model_after250000.zip', 
    'logs/PPO-Acc-0.533-0.682-0.719-1649886510/model_after250000.zip', 
    'logs/PPO-Acc-0.683-0.722-0.53-1649884621/model_after250000.zip', 
    'logs/PPO-Acc-0.712-0.558-0.65-1649885261/model_after250000.zip', 

]

for count, i in enumerate(target_dicts):
    # Load the trained agent
    model = PPO.load(trained_agent[count],  device = 'cuda')
    
    target_dict = target_dicts[count]
    # Environment initialization
    env_id = f'PPO-Gazebo-Acc-{target_dict[0].x}-{target_dict[0].y}-{target_dict[0].z}-{int(time.time())}'

    env = ContinuousArmMotionEnvironment(sim_type='Gazebo', target_dict = target_dict, save_to_disk=True, env_id = env_id)
    model.set_env(env)
    
    # eval_callback = EvalCallback(env, best_model_save_path=f'./best_model-{env_id}/',
    #                             log_path=f'./-{env_id}/', eval_freq=200,
    #                             deterministic=True, render=False)

    # Get baseline for how far off the trained model is
    obs = env.reset()

    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        init_distance = env.S.distance_from_target(target_dict[0])

    autosave_path = os.path.join('logs', env_id, f'model_after{time_steps}')

    start = time.time()

    model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)
    end = time.time()

    model.save(autosave_path)

    print(f'Autosaved at {len(env.hist_list)} episodes')

    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        final_distance = env.S.distance_from_target(target_dict[0])

    print(f'Init dist - {init_distance}- Final dist - {final_distance}')

    os.makedirs(os.path.join('logs', env_id, f'Init dist - {init_distance}- Final dist - {final_distance}'))

    shutil.copyfile('logs/reward.csv', os.path.join('logs', env_id, 'rewards.csv'))

    os.makedirs(os.path.join('logs', env_id, f'Runtime_was_{end-start}'))
