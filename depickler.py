import pickle
import os
import matplotlib.pyplot as plt
import pandas as pd

package_dir = 'results'

for package in os.listdir(package_dir):
    try:
        pack_dir = os.path.join(package_dir, package)
        env = pickle.load(open(os.path.join(pack_dir,'env_autosave.p'), 'rb'))
        env.plot_rewards('')
        plt.savefig(os.path.join(pack_dir,f'Rewards-{package}.png'))
        plt.close()
        env.hist_list[-1].plot_episode_3D()
        plt.savefig(os.path.join(pack_dir,f'Last_Ep-{package}.png'))
        plt.close()

        print(f'{package} - {env.hist_list[-1].start_time-env.hist_list[0].start_time}')

        # print(env.hist_list[0].)
    except Exception as e:
        pass
    try:
        pack_dir = os.path.join(package_dir, package)
        env_hist_list = pickle.load(open(os.path.join(pack_dir,'env_hist_list_autosave.p'), 'rb'))
        env_hist_list[-1].plot_episode_3D()
        plt.savefig(os.path.join(pack_dir,f'Last_Ep-{package}.png'))
        plt.close()
        
        print(f'{package} - {env_hist_list[-1].start_time-env_hist_list[0].start_time}')
    except:
        pass
    try:
        rewards = pd.read_csv(os.path.joint(pack_dir, 'rewards.csv'))
        plt.plot(rewards['Reward'])
        plt.savefig(os.path.join(pack_dir,f'Rewards-{package}.png'))
        plt.close()

        # print(f'{package} - {env_hist_list[-1].start_time-env_hist_list[0].start_time}')
    except Exception as e:
        pass



