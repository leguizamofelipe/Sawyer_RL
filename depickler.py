import pickle
import os
import matplotlib.pyplot as plt

package_dir = 'packages'

for package in os.listdir(package_dir):
    try:
        pack_dir = os.path.join(package_dir, package)
        hist_list = pickle.load(open(os.path.join(pack_dir,'env_hist_list_autosave.p'), 'rb'))
        hist_list[-3].plot_episode_3D()
        plt.savefig(os.path.join(pack_dir,f'{package}.png'))
        plt.close()
    except Exception as e:
        print(e)
        print(f'Failed to load env for {package}')
