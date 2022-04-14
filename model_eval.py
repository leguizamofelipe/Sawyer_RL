from turtle import done
from stable_baselines3 import SAC
from torch import device
from sawyer_continuous_env import *
from stable_baselines3 import PPO

trained_agent = ['best_model/best_model.zip'] 
target_dicts = [{ 0: Point(0.590,0.734,0.630)}]

# Load the trained agent
model = SAC.load('logs\SAC-0.1-0.1-0.1-1649633921\model_after500.zip')

target_dict = target_dicts[0]
# Environment initialization
env_id = str(time.time())

env = ContinuousArmMotionEnvironment(sim_type='DH', target_dict = target_dict, save_to_disk=True, env_id = env_id)
model.set_env(env)

# Get baseline for how far off the trained model is
obs = env.reset()

done = False
while not done:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    init_distance = env.S.distance_from_target(target_dict[0])

model.learn(total_timesteps=400, n_eval_episodes = 30)

autosave_path = os.path.join('logs', env_id, 'Autosave')
