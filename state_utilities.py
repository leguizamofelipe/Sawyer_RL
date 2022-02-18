from ntpath import join
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Utilities for determining number of states, needed for Q function

# from sawyer_env import m_f
results_array = {}

m_f = 0.3

def find_num_states(m_f):
    joint_positions = {
        '0' : np.arange(  0 , 1.5  + m_f , m_f ),
        '1' : np.arange( -1 ,  1   + m_f , m_f ),
        # '2' : np.arange( -3 ,  3   + m_f , m_f ),
        '3' : np.arange( -2 ,  2   + m_f , m_f ),
        # '4' : np.arange( -2 ,  2   + m_f , m_f ),
        '5' : np.arange( -2 ,  2   + m_f , m_f ),
        # '6' : np.arange( -3 ,  3   + m_f , m_f ),
    }

    num_pos = [len(joint_positions[key]) for key in joint_positions]

    # states = np.prod(num_pos)

    states = 1
    for num in num_pos:
        states = states * num

    results_array.update({m_f : states})

    return states

states = find_num_states(m_f)

print(states)