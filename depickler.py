import pickle
import os
import matplotlib.pyplot as plt

package_dir = 'packages'

for package in os.listdir(package_dir):
    try:
        pack_dir = os.path.join(package_dir, package)
        env = pickle.load(open(os.path.join(pack_dir,'env_autosave.p'), 'rb'))
        env.plot_rewards('')
        plt.savefig(os.path.join(pack_dir,f'{package}.png'))
    except Exception as e:
        print(e)
        print(f'Failed to load env for {package}')
