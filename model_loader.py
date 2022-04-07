from sawyer_continuous_env import *
from point import Point
from stable_baselines.common.evaluation import evaluate_policy

from stable_baselines3 import PPO

target_dict = { 0: Point(0.7315905137589676, 0.7115280197260334, 0.15348379395482878),
                1: Point(0.7801117441176564, 0.5500329764864156, 0.1842536897312016 ),
                2: Point(0.685123322687442,  0.6840350631055033, 0.47147110493178634)}

# Load the trained agent
model = PPO.load("n1_Points_PPO.zip")

env = model.get_env()

# Evaluate the agent
# mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    # env.render()

