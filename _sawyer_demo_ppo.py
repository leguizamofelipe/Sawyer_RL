from sawyer_continuous_env import *
from point import Point

from stable_baselines3 import PPO

for target_dict in [{ 0: Point(0.683,0.722,0.530)}, { 0: Point(0.590, 0.734, 0.630)}, { 0: Point(0.533, 0.682, 0.719)}]: 
                    
    start=time.time()

    time_steps = 500000

    if len(target_dict) ==1:
        env_id = f'PPO-Gazebo-From-Scratch-{target_dict[0].x}-{target_dict[0].y}-{target_dict[0].z}-{int(time.time())}'

    env = ContinuousArmMotionEnvironment(sim_type = 'Gazebo', target_dict=target_dict, env_id=env_id)

    model = PPO('MlpPolicy', env, verbose = 1, device = 'cuda')

    model.learn(total_timesteps=int(time_steps), n_eval_episodes = 30)

    model.save(os.path.join('logs', env_id, f'model_after{model.num_timesteps}'))

    end = time.time()

    print(f'Runtime = {end-start}')
    
    os.makedirs(os.path.join('logs', env_id, f'Runtime_was_{end-start}'))

    