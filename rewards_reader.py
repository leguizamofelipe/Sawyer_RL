from turtle import width
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from point import Point
import math

search_dir = 'packages'

def distance_from_target(target, endpoint):
    # Current position
    c = endpoint

    # Target position
    t = target

    distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
    
    return distance

for title in ['rewards.csv', 'reward.csv']:
    for package in os.listdir(search_dir):
        try:
            df = pd.read_csv(os.path.join(search_dir, package, title))
            train_time = - float(df['Time Started'][0]) + float(list(df['Time Started'])[-1])
            plt.plot(df['Reward'], alpha = 1, linewidth=0.2)
            plt.xlabel('Episode')
            plt.ylabel('Reward')
            ep_count = len(df['Reward'])
            plt.title(f'Rewards per episode for {ep_count} episodes\n Train time = {round(train_time, 2)} s')
            plt.tight_layout()
            plt.savefig(os.path.join(search_dir, package, 'rewards.png'))
            plt.close()

            p = df['Target Pos'][0].split(' ')
            target = Point(float(p[1]), float(p[3]), float(p[5]))
            
            distance_list = []
            for point in df['Ending Pos']:
                p = point.split(' ')
                p = Point(float(p[1]), float(p[3]), float(p[5]))
                distance = distance_from_target(target, p)
                distance_list.append(distance)

            plt.plot(distance_list, alpha = 1, linewidth=0.2)
            plt.xlabel('Episode')
            plt.ylabel('Distance (m)')
            ep_count = len(df['Reward'])
            plt.title(f'Distance from target for {ep_count} episodes\n Train time = {round(train_time, 2)} s')
            plt.tight_layout()
            plt.savefig(os.path.join(search_dir, package, 'distances.png'))
            plt.close()
            
        except Exception as e:
            pass
