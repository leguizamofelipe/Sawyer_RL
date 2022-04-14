import pandas as pd
import pickle
import os
import numpy as np
import math
from point import Point

def distance(endpoint, target):
    # Current position
    c = endpoint

    # Target position
    t = target

    distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
    
    return distance

ppo_results = [
    # 'results\PPO-0.59-0.734-0.63-1649388342',
    # 'results\PPO-0.533-0.682-0.719-1649521198',
    # 'results\PPO-0.657-0.712-0.719-1649519423',
    # 'results\PPO-0.683-0.722-0.53-1649386439',
    # 'results\PPO-0.712-0.558-0.65-1649655599',
    # 'results\PPO-Gazebo-0.59-0.734-0.63-1649427271',
    # 'results\PPO-Gazebo-0.533-0.682-0.719-1649537914',
    # 'results\PPO-Gazebo-0.683-0.722-0.53-1649398856',
    # 'results\PPO-Gazebo-0.712-0.558-0.65-1649567999',
    # 'results\PPO-Gazebo-0.712-0.558-0.65-1649612055',
    # 'results\PPO-Gazebo-From-Scratch-0.59-0.734-0.63-1649726012',
    # 'results\PPO-Gazebo-From-Scratch-0.533-0.682-0.719-1649749108',
    # 'results\PPO-Gazebo-From-Scratch-0.683-0.722-0.53-1649704047',
    # 'results\PPO-Gazebo-From-Scratch-10pts-1649709026',
    # 'results\PPO-Gazebo-From-Scratch-50pts-1649708539',
    # 'results\SAC-0.59-0.734-0.63-1649645909',
    # 'results\SAC-0.515-0.525-0.721-1649712843',
    # 'results\SAC-0.533-0.682-0.719-1649697597',
    # 'results\SAC-0.683-0.722-0.53-1649636642',
    # 'results\SAC-0.712-0.558-0.65-1649641248',
    # 'results\SAC-Gazebo-0.59-0.734-0.63-1649658658',
    # 'results\SAC-Gazebo-0.515-0.525-0.721-1649816975',
    # 'results\SAC-Gazebo-0.533-0.682-0.719-1649796036',
    # 'results\SAC-Gazebo-0.683-0.722-0.53-1649678544',
    # 'results\SAC-Gazebo-0.712-0.558-0.65-1649775613',
    # 'results\PPO-Acc-0.59-0.734-0.63-1649885884',
    # 'results\PPO-Acc-0.515-0.525-0.721-1649887136',
    # 'results\PPO-Acc-0.533-0.682-0.719-1649886510',
    # 'results\PPO-Acc-0.683-0.722-0.53-1649884621',
    # 'results\PPO-Acc-0.712-0.558-0.65-1649885261',

    'results\PPO-Gazebo-Acc-0.59-0.734-0.63-1649894756',
    'results\PPO-Gazebo-Acc-0.515-0.525-0.721-1649903718',
    'results\PPO-Gazebo-Acc-0.533-0.682-0.719-1649912170',
    'results\PPO-Gazebo-Acc-0.683-0.722-0.53-1649921274',
    'results\PPO-Gazebo-Acc-0.712-0.558-0.65-1649930631',

]

for file in ppo_results:
    try:
        try:
            env = pickle.load(open(os.path.join(file,'env_autosave.p'), 'rb'))
            env = env.hist_list
        except:
            env = pickle.load(open(os.path.join(file,'env_hist_list_autosave.p'), 'rb'))
        
        ep_list = range(0, len(env))
        time_list = np.array([t.start_time for t in env])
        time_list_since_start = time_list-time_list[0]
        reward_list = [x.total_reward() for x in env]
        distance_list = []
        for i in range(0, len(env)):
            try:
                distance_list.append(distance(env[i].endpoint_history[-1], env[i].target))
            except:
                distance_list.append(distance(Point(0,0,0), env[i].target))
                print(i)
        
        df = pd.DataFrame({'Episode' : ep_list, 'Time' : time_list, 'TimeZeroed' : time_list_since_start, 'Reward' : reward_list, 'Distance' : distance_list})

        df.to_csv(os.path.join(file, 'results_sum.csv'))
    except:
        pass
