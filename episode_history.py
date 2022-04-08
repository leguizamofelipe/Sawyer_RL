import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
from mpl_toolkits import mplot3d
import time


class EpisodeHistory():
    def __init__(self, ep_no, init, target) -> None:
        self.ep_no = ep_no
        self.endpoint_history = []
        self.reward_history = []
        self.cumulative_reward_history = []
        self.first_timestep = True
        self.target = target
        self.init = init
        self.start_time = time.time()
    def record_endpoint(self, endpoint):
        self.endpoint_history.append(endpoint)
    def record_reward(self, reward):
        self.reward_history.append(reward)
        if self.first_timestep:
            self.prev_reward = 0
            self.first_timestep = False
        else:
            self.prev_reward = self.cumulative_reward_history[-1]
        self.cumulative_reward_history.append(reward + self.prev_reward)
    def total_reward(self):
        return sum(self.reward_history)
    def record_steps(self, steps):
        self.final_steps = steps
    def plot_episode_3D(self):
        ax = plt.axes(projection = '3d')
        ax.set_xlim([0,1]) # Was 0.5
        ax.set_ylim([0,1]) # Was 0.5
        ax.set_zlim([0,1])
        x_list = [point.x for point in self.endpoint_history]
        y_list = [point.y for point in self.endpoint_history]
        z_list = [point.z for point in self.endpoint_history]
        ax.plot3D(x_list, y_list, z_list, 'blue')
        ax.scatter3D(self.init.x, self.init.y, self.init.z, color = 'r')
        ax.scatter3D(self.target.x, self.target.y, self.target.z, color = 'g')
        ax.set_title(f'n_steps: {len(self.endpoint_history)} | reward: {self.cumulative_reward_history[-1]}')
        plt.tight_layout()
        plt.show()
        