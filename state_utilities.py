from ntpath import join
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
# Utilities for determining number of states, needed for Q function

# from sawyer_env import m_f
results_array = {}

# m_f = 0.3

def find_num_states(m_f, joint_positions):

    states_matrix  = np.array(list(itertools.product(*list(joint_positions.values()), repeat=1)))
    states_matrix = np.around(states_matrix, 1)

    states_dict = {}
    for count, state in enumerate(states_matrix):
        states_dict.update({count:state})

    num_pos = [len(joint_positions[key]) for key in joint_positions]

    # states = np.prod(num_pos)

    states = 1
    for num in num_pos:
        states = states * num

    results_array.update({m_f : states})

    return states, states_dict

# states = find_num_states(m_f)
