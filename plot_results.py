import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

results = pd.read_csv('Sawyer_RL/logs/reward_21k_timesteps.csv')

plt.plot(results.index, results['Reward'])
plt.title(f'Rewards vs time for {len(results)} episodes')
plt.xlabel('Episode')
plt.ylabel('Reward')

x = results.index
y = results['Reward']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.tight_layout()
plt.show()