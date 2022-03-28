import torch
from torch import nn
from pfrl.agents.ddpg import DDPG
from pfrl.nn import BoundByTanh, ConcatObsAndAction
from pfrl.policies import DeterministicHead
from pfrl import experiments, explorers, replay_buffers, utils
from sawyer_continuous_env import *

#################### ENVIRONMENT DEFINITION ##########################

env = ContinuousArmMotionEnvironment()

######################## AGENT DEFINITION ################################

q_func = nn.Sequential(
    ConcatObsAndAction(),
    nn.Linear(env.observation_space.n + env.action_space.n, 400),
    nn.ReLU(),
    nn.Linear(400, 300),
    nn.ReLU(),
    nn.Linear(300, 1),
)
policy = nn.Sequential(
    nn.Linear(env.observation_space.n, 400),
    nn.ReLU(),
    nn.Linear(400, 300),
    nn.ReLU(),
    nn.Linear(300, env.action_space.n),
    BoundByTanh(low=env.action_space.low, high=env.action_space.high),
    DeterministicHead(),
)

opt_a = torch.optim.Adam(policy.parameters())
opt_c = torch.optim.Adam(q_func.parameters())

rbuf = replay_buffers.ReplayBuffer(10**6)

explorer = explorers.AdditiveGaussian(
    scale=0.1, low=env.action_space.low, high=env.action_space.high
)

def burnin_action_func():
    """Select random actions until model is updated one or more times."""
    return np.random.uniform(env.action_space.low, env.action_space.high).astype(np.float32)

# Hyperparameters in http://arxiv.org/abs/1802.09477
agent = DDPG(
    policy,
    q_func,
    opt_a,
    opt_c,
    rbuf,
    gamma=0.99,
    explorer=explorer,
    replay_start_size=10000, #Default from example 
    target_update_method="soft",
    target_update_interval=1,
    update_interval=1,
    soft_update_tau=5e-3,
    n_times_update=1,
    gpu=-1,
    minibatch_size=100,
    burnin_action_func=burnin_action_func,
)

total_timesteps = 10e6
timestep_limit = 100

experiments.train_agent_with_evaluation(
            agent=agent,
            env=env,
            steps=total_timesteps,
            eval_env=env,
            eval_n_steps=None,
            eval_n_episodes=10,
            eval_interval=100,
            outdir='/out',
            train_max_episode_len=timestep_limit,
        )

print('done?')