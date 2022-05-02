from turtle import width
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.pyplot import figure

import matplotlib
matplotlib.rcParams.update({'font.size': 18})

############ Plots ######################
# Superimposed DH plots for all 5 points (PPO)
# Superimposed Gazebo plots for all 5 points (PPO)
# Superimposed DH plots for all 5 points (SAC)
# Superimposed Gazebo plots for all 5 points (SAC)
# Distance improvement (DH + Gazebo)


############################################################################################
############################################################################################
#########################  PPO Trained with DH #############################################
############################################################################################
############################################################################################
# ppo_dh = [
#     # 'results\PPO-0.59-0.734-0.63-1649388342',
#     # 'results\PPO-0.515-0.525-0.721-1649654119',
#     # 'results\PPO-0.533-0.682-0.719-1649521198',
#     # 'results\PPO-0.683-0.722-0.53-1649386439',
#     # 'results\PPO-0.712-0.558-0.65-1649655599',

#     'results\PPO-Acc-0.59-0.734-0.63-1649885884',
#     'results\PPO-Acc-0.515-0.525-0.721-1649887136',
#     'results\PPO-Acc-0.533-0.682-0.719-1649886510',
#     'results\PPO-Acc-0.683-0.722-0.53-1649884621',
#     'results\PPO-Acc-0.712-0.558-0.65-1649885261',
# ]

# col = ['blue', 'orange', 'purple', 'green', 'red']
# figure(figsize=(10, 8), dpi=80)

# for count, file in enumerate(ppo_dh):
#     s = file.split('-')
#     df = pd.read_csv(os.path.join(file, 'results_sum.csv'))
#     df['Rolling Average'] = df['Reward'].rolling(100).mean()
#     plt.plot(df['Timestep'], df['Reward'], alpha=0.3, linewidth =0.2, color = col[count])
#     plt.plot(df['Timestep'], df['Rolling Average'], alpha=0.9, linewidth = 3, color = col[count], label = f'({float(s[2]):.3f}, {float(s[3]):.3f}, {float(s[4]):.3f})')
#     plt.xlabel('Step')
#     plt.ylabel('Reward')
#     plt.xlim(0, 200000)
#     plt.xticks(np.arange(0, 200001, step=50000))
#     plt.ylim(-1000, 250)
#     plt.tight_layout()
#     plt.legend()

# plt.savefig('plots/ppo_dh_acc_combined_plot.png', dpi = 250)

# plt.close()


# ############################################################################################
# ############################################################################################
# #########################  PPO from Gazebo scratch #########################################
# ############################################################################################
# ############################################################################################

# ppo_gazebo_scratch = [
#     'results\PPO-Gazebo-From-Scratch-0.59-0.734-0.63-1649726012',
#     'results\PPO-Gazebo-From-Scratch-0.515-0.525-0.721-1649948547',
#     'results\PPO-Gazebo-From-Scratch-0.533-0.682-0.719-1649749108',
#     'results\PPO-Gazebo-From-Scratch-0.683-0.722-0.53-1649704047',
#     'results\PPO-Gazebo-From-Scratch-0.712-0.558-0.65-1649963242'
# ]

# figure(figsize=(10, 8), dpi=80)

# for count, file in enumerate(ppo_gazebo_scratch):
#     s = file.split('-')
#     df = pd.read_csv(os.path.join(file, 'results_sum.csv'))
#     df['Rolling Average'] = df['Reward'].rolling(100).mean()
#     plt.plot(df['Timestep'], df['Reward'], alpha=0.3, linewidth =0.3, color = col[count])
#     plt.plot(df['Timestep'], df['Rolling Average'], alpha=0.9, linewidth = 3, color = col[count], label = f'({float(s[4]):.3f}, {float(s[5]):.3f}, {float(s[6]):.3f})')
#     plt.xlabel('Step')
#     plt.ylabel('Reward')
#     plt.ylim(-1000, 250)
#     plt.tight_layout()
#     plt.legend()

# plt.savefig('plots/ppo_gazebo_from_scratch_combined_plot.png', dpi = 250)

# plt.close()

# ############################################################################################
# ############################################################################################
# #########################  PPO DH + Gazebo transfer ########################################
# ############################################################################################
# ############################################################################################


# ppo_pairs = [
#     ['results\PPO-Acc-0.59-0.734-0.63-1649885884',    'results\PPO-Gazebo-Acc-0.59-0.734-0.63-1649894756',   'results\PPO-Gazebo-From-Scratch-0.59-0.734-0.63-1649726012'],
#     ['results\PPO-Acc-0.515-0.525-0.721-1649887136',  'results\PPO-Gazebo-Acc-0.515-0.525-0.721-1649903718', 'results\PPO-Gazebo-From-Scratch-0.515-0.525-0.721-1649948547'],
#     ['results\PPO-Acc-0.533-0.682-0.719-1649886510',  'results\PPO-Gazebo-Acc-0.533-0.682-0.719-1649912170', 'results\PPO-Gazebo-From-Scratch-0.533-0.682-0.719-1649749108'],
#     ['results\PPO-Acc-0.683-0.722-0.53-1649884621',   'results\PPO-Gazebo-Acc-0.683-0.722-0.53-1649921274',  'results\PPO-Gazebo-From-Scratch-0.683-0.722-0.53-1649704047'],
#     ['results\PPO-Acc-0.712-0.558-0.65-1649885261',   'results\PPO-Gazebo-Acc-0.712-0.558-0.65-1649930631',  'results\PPO-Gazebo-From-Scratch-0.712-0.558-0.65-1649963242'],
# ]

# for count, pair in enumerate(ppo_pairs):
#     figure(figsize=(10, 8), dpi=80)

#     dh_df = pd.read_csv(os.path.join(pair[0], 'results_sum.csv'))
#     gazebo_df = pd.read_csv(os.path.join(pair[1], 'results_sum.csv'))
#     if pair[2] == '':
#         pass
#     else:
#         gazebo_scratch_df = pd.read_csv(os.path.join(pair[2], 'results_sum.csv'))
#     plt.axvline(x=np.array(dh_df['TimeZeroed'])[-1], color = 'red')
#     rewards = pd.concat((dh_df['Reward'], gazebo_df['Reward']))
#     rewards_rolling_average = rewards.rolling(50).mean()
    
#     time = pd.concat((dh_df['TimeZeroed'], gazebo_df['TimeZeroed'] - gazebo_df['TimeZeroed'][0] + dh_df['TimeZeroed'][len(dh_df)-1]))
#     time = time.reset_index(drop=True)

#     s = pair[1].split('-')

#     # df['Rolling Average'] = df['Reward'].rolling(100).mean()
#     plt.plot(time, rewards, alpha=0.2, linewidth =0.3, color = 'blue')
#     plt.plot(time, rewards_rolling_average, alpha=0.9, linewidth =3, color = 'blue', label = 'Training with DH Model + Transfer to Gazebo')
#     if pair[2] == '':
#         pass
#     else:
#         plt.plot(gazebo_scratch_df['TimeZeroed'], gazebo_scratch_df['Reward'], color = 'black', alpha = 0.3, linewidth = 0.3)
#         gazebo_scratch_df['RollingAverage'] = gazebo_scratch_df['Reward'].rolling(100).mean()
#         plt.plot(gazebo_scratch_df['TimeZeroed'], gazebo_scratch_df['RollingAverage'], alpha = 0.9, color = 'black', linestyle = 'dotted', linewidth = 3, label = 'Training Exclusively in Gazebo')
#     # plt.plot(df['Rolling Average'], alpha=0.9, linewidth = 3, color = col[count], label = f'({s[2]}, {s[3]}, {s[4]})')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Reward')
#     plt.ylim(-1000, 250)
#     plt.xlim(0, 10000)
#     plt.tight_layout()
#     plt.legend()
#     i = pair[0].split('\\')[1]
#     plt.savefig(f'plots/Transfer-{i}.png', dpi = 250)
#     plt.close()

# # figure(figsize=(10, 8), dpi=80)

# col = ['blue', 'green', 'purple', 'green', 'red']

# sac_dh = [
#     'results\PPO-Sawyer-From-Scratch-0.59-0.734-0.63-1649871813',
#     'results\PPO-Sawyer-From-Scratch-0.683-0.722-0.53-1649711359',
#     'results\PPO-Sawyer-From-Scratch-0.533-0.682-0.719-1650409278',
# ]
# figure(figsize=(10, 8), dpi=80)

# for count, file in enumerate(sac_dh):
#     s = file.split('-')
#     df = pd.read_csv(os.path.join(file, 'results_sum.csv'))
#     df['Rolling Average'] = df['Reward'].rolling(100).mean()
#     plt.plot(df['Timestep'], df['Reward'], alpha=0.3, linewidth =0.3, color = col[count])
#     plt.plot(df['Timestep'], df['Rolling Average'], alpha=0.9, linewidth = 3, color = col[count], label = f'({float(s[4]):.3f}, {float(s[5]):.3f}, {float(s[6]):.3f})')
#     plt.xlabel('Step')
#     plt.ylabel('Reward')
#     plt.ylim(-1000, 250)
#     plt.xlim(0, 250000)
#     plt.tight_layout()
#     plt.legend()

# plt.savefig('plots/sawyer_hardware_combined_plot.png', dpi = 250)

# plt.close()
# '''
# sac_pairs = [
#     ['results\SAC-0.59-0.734-0.63-1649645909',     'results\SAC-Gazebo-0.59-0.734-0.63-1649658658'],
#     ['results\SAC-0.515-0.525-0.721-1649712843',   'results\SAC-Gazebo-0.515-0.525-0.721-1649816975'],
#     ['results\SAC-0.533-0.682-0.719-1649697597',   'results\SAC-Gazebo-0.533-0.682-0.719-1649796036'],
#     ['results\SAC-0.683-0.722-0.53-1649636642',    'results\SAC-Gazebo-0.683-0.722-0.53-1649678544'],
#     ['results\SAC-0.712-0.558-0.65-1649641248',    'results\SAC-Gazebo-0.712-0.558-0.65-1649775613'],
# ]

# col = ['blue', 'orange', 'purple', 'green', 'red']

# for count, pair in enumerate(sac_pairs):
#     figure(figsize=(10, 8), dpi=80)
#     dh_df = pd.read_csv(os.path.join(pair[0], 'results_sum.csv'))
#     gazebo_df = pd.read_csv(os.path.join(pair[1], 'results_sum.csv'))

#     rewards = pd.concat((dh_df['Reward'], gazebo_df['Reward']))
#     time = pd.concat((dh_df['TimeZeroed'], gazebo_df['TimeZeroed'] - gazebo_df['TimeZeroed'][0] + dh_df['TimeZeroed'][len(dh_df)-1]))
#     time = time.reset_index(drop=True)

#     s = pair[1].split('-')

#     # df['Rolling Average'] = df['Reward'].rolling(100).mean()
#     plt.plot(time, rewards, alpha=1, linewidth =0.5, color = col[count], label = f'({s[2]}, {s[3]}, {s[4]})')
#     # plt.plot(df['Rolling Average'], alpha=0.9, linewidth = 3, color = col[count], label = f'({s[2]}, {s[3]}, {s[4]})')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Reward')
#     plt.ylim(-1000, 200)
#     plt.tight_layout()
#     plt.legend()
#     plt.savefig(f'plots/sac_gazebo_from_dh_combined_plot-{s[2]}-{s[3]}-{s[4]}.png', dpi = 250)
#     plt.close()

# '''

col = ['blue', 'orange', 'purple', 'green', 'red']

multiple_points_scratch = [
    'results\PPO-Gazebo-From-Scratch-10pts-1649709026',
    'results\PPO-Gazebo-From-Scratch-10pts-1649790060',
    'results\PPO-Gazebo-From-Scratch-50pts-1649708539'
]


for count, file in enumerate(multiple_points_scratch):
    figure(figsize=(10, 8), dpi=80)

    s = file.split('-')
    df = pd.read_csv(os.path.join(file, 'results_sum.csv'))
    df['Rolling Average'] = df['Reward'].rolling(100).mean()
    plt.plot(df['Timestep'], df['Reward'], alpha=0.3, linewidth =0.3, color = col[count])
    plt.plot(df['Timestep'], df['Rolling Average'], alpha=0.9, linewidth = 3, color = col[count], label = f'{s[4][0:2]} Points')
    plt.xlabel('Step')
    plt.ylabel('Reward')
    plt.ylim(-1000, 250)
    plt.xlim(0, 5e6)
    plt.tight_layout()
    plt.legend()
    plt.savefig(f'plots/ppo_multiple_points-{s[-1]}.png', dpi = 250)
    plt.close()

plt.close()