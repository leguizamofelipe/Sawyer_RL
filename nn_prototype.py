from sawyer_dqn_env import *

import pfrl
import torch
import torch.nn
import gym
import numpy

gamma = 0.9
epsilon = 0.3

env = DQNArmMotionEnvironment()

class QFunction(torch.nn.Module):

    def __init__(self, obs_size, n_actions):
        super().__init__()
        self.l1 = torch.nn.Linear(obs_size, 200)
        self.l2 = torch.nn.Linear(200, 200)
        self.l3 = torch.nn.Linear(200, n_actions)

    def forward(self, x):
        h = x
        h = torch.nn.functional.relu(self.l1(h))
        h = torch.nn.functional.relu(self.l2(h))
        h = self.l3(h)
        return pfrl.action_value.DiscreteActionValue(h)


obs_size = env.observation_space.n
n_actions = env.action_space.n
q_func = QFunction(obs_size, n_actions)

optimizer = torch.optim.Adam(q_func.parameters(), eps=1e-2)

# What do these do?
explorer = pfrl.explorers.ConstantEpsilonGreedy(
    epsilon, random_action_func=env.action_space.sample)
replay_buffer = pfrl.replay_buffers.ReplayBuffer(capacity=10 ** 6)
def phi(x): return x.astype(numpy.float32, copy=False)

gpu = -1

agent = pfrl.agents.DoubleDQN(
    q_func,
    optimizer,
    replay_buffer,
    gamma,
    explorer,
    replay_start_size=500,
    update_interval=1,
    target_update_interval=100,
    phi=phi,
    gpu=gpu,
)

ep_reward_list = []

n_episodes = 1000000
max_ep_len = 50
ep_hist_list = []

for episode in range(n_episodes):
    observation = env.reset()
    ep_hist = EpisodeHistory(episode, env.init_pos, env.target_pos)
    step = 0
    while True:
        action = agent.act(observation)
        observation, reward, done = env.step(action)
        reset = step == max_ep_len-1
        agent.observe(observation, reward, done, reset)
        ep_hist.record_reward(reward)
        ep_hist.record_endpoint(env.S.endpoint)
        if done or reset:
            ep_hist.record_steps(step)
            break
        step+=1
    ep_hist_list.append(ep_hist)
    print(f"    *Episode {episode}: reward {ep_hist.total_reward()}, target {env.target_pos} reached? {done}")

rewards_list = [episode.total_reward() for episode in ep_hist_list]

ax = plt.axes()
ax.plot(rewards_list)

print('done')
