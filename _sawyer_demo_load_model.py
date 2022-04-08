from torch import device
from sawyer_continuous_env import *
from stable_baselines3 import PPO

time_steps = 10e6
save_rate = 50000

# Load the trained agent
model = PPO.load("n1_Points_PPO.zip",  device = 'cuda')
first_loop = True

for i in range(1, int(time_steps/save_rate)):
    if first_loop:
        pass
    else:
        model = PPO.load("Autosave.zip",  device = 'cuda')
    
    target_dict = { 0: Point(0.602,0.681,0.317)}

    env = ContinuousArmMotionEnvironment(sim_type='Gazebo', target_dict = target_dict, save_to_disk=True)

    model.set_env(env)
    try:
        model.learn(total_timesteps=int(save_rate), n_eval_episodes = 30)
    except:
        pass

    model.save('Autosave')

# Enjoy trained agent
obs = env.reset()
for i in range(100):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)

print('Done')