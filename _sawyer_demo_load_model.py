from sawyer_continuous_env import *
from stable_baselines3 import PPO

# Load the trained agent
model = PPO.load("n1_Points_PPO.zip")

# Target - Point(0.602,0.681,0.317)

env = ContinuousArmMotionEnvironment(sim_type='Gazebo')

# Enjoy trained agent
obs = env.reset()
for i in range(100):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)

print('Done')