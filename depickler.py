import pickle
import os
import matplotlib.pyplot as plt
import pandas as pd

package_dir = 'packages'
for name in ['env_autosave.p', 'env_hist_list_autosave.p']:
    for package in os.listdir(package_dir):
        
        try:
            pack_dir = os.path.join(package_dir, package)
            env = pickle.load(open(os.path.join(pack_dir,name), 'rb'))
            env.plot_rewards('')
            plt.savefig(os.path.join(pack_dir,f'Rewards-{package}.png'))
            plt.close()
            env.hist_list[-1].plot_episode_3D()
            plt.savefig(os.path.join(pack_dir,f'Last_Ep-{package}.png'))
            plt.close()
        except Exception as e:
            pass
        try:
            pack_dir = os.path.join(package_dir, package)
            env_hist_list = pickle.load(open(os.path.join(pack_dir,name), 'rb'))
            env_hist_list[-1].plot_episode_3D()
            plt.savefig(os.path.join(pack_dir,f'Last_Ep-{package}.png'))
            plt.close()
        except:
            pass
        try:
            rewards = pd.read_csv(os.path.joint(pack_dir, 'rewards.csv'))
            plt.plot(rewards['Reward'])
            plt.savefig(os.path.join(pack_dir,f'Rewards-{package}.png'))
            plt.close()
        except Exception as e:
            pass

