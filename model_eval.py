from turtle import done
from torch import device
from sawyer_continuous_env import *
from stable_baselines3 import PPO

trained_agent = ['best_model/best_model.zip'] 
target_dicts = [{ 0: Point(0.766,0.525,0.781)}]

# Load the trained agent
model = PPO.load('best_model/best_model.zip')

target_dict = target_dicts[0]
# Environment initialization
env_id = f'Burner'

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
