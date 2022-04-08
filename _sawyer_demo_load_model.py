from torch import device
from sawyer_continuous_env import *
from stable_baselines3 import PPO

time_steps = 500000
save_rate = 50000

# USER DEFINED SECTION
trained_agent = 'logs/n1_Points_PPO.zip'
# ********************************************************
# Load the trained agent
model = PPO.load(trained_agent,  device = 'cuda')
first_loop = True

target_dict = { 0: Point(0.707,0.712,0.719)}

env = ContinuousArmMotionEnvironment(sim_type='Gazebo', target_dict = target_dict, save_to_disk=True)

for i in range(1, int(time_steps/save_rate) + 1):
    if first_loop:
        pass
    else:
        model = PPO.load("Autosave.zip",  device = 'cuda')

    model.set_env(env)
    try:
        model.learn(total_timesteps=int(save_rate), n_eval_episodes = 30)
    except:
        pass

    model.save('Autosave')
    print(f'Autosaved at {len(env.hist_list)}')