from turtle import done
from torch import device
from sawyer_continuous_env import *
from stable_baselines3 import PPO
import shutil

time_steps = 300000
save_rate = 10000

# ****************** USER DEFINED SECTION ***************
# trained_agent = ['logs/PPO-0.533-0.792-0.719-1649451317/model_after501760.zip', 'logs/PPO-0.766-0.525-0.781-1649453106/model_after501760.zip'] 
# ********************************************************

trained_agent = ['logs/PPO-0.766-0.525-0.781-1649453106/model_after501760.zip'] 
target_dicts = [{ 0: Point(0.766,0.525,0.781)}]

for count, i in enumerate(target_dicts):
    # Load the trained agent
    model = PPO.load(trained_agent[count],  device = 'cuda')
    
    target_dict = target_dicts[count]
    # Environment initialization
    env_id = f'PPO-Gazebo-{target_dict[0].x}-{target_dict[0].y}-{target_dict[0].z}-{int(time.time())}'

    env = ContinuousArmMotionEnvironment(sim_type='Gazebo', target_dict = target_dict, save_to_disk=True, env_id = env_id)
    model.set_env(env)

    # Get baseline for how far off the trained model is
    obs = env.reset()

    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        init_distance = env.S.distance_from_target(target_dict[0])

    autosave_path = os.path.join('logs', env_id, 'Autosave')

    first_loop = True
    for i in range(1, int(time_steps/save_rate) + 1):
        if first_loop:
            first_loop = False
        else:
            model = PPO.load(autosave_path,  device = 'cuda')
            model.set_env(env)

        try:
            model.learn(total_timesteps=int(save_rate), n_eval_episodes = 30)
        except Exception as e:
            print(e)

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
