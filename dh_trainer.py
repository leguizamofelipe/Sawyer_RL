import numpy as np
import pandas as pd
from kinematics_from_dh import *
import pickle

thetas = [0.75, 0, 0, 0, 0, 0, 0]

a_1 = 0.081
alpha_1 = -90 
alpha_2 =  90 
alpha_3 = -90 
alpha_4 =  90 
alpha_5 = -90 
alpha_6 =  90 

d_0 =   0.317   
d_1 =   0.192501
d_2 =   0.4     
d_3 =  -.1683   
d_4 =   0.4     
d_5 =   0.1360  
d_6 =   0.2701  

points_dict = pickle.load(open('points.p', ''))

sawyer_dh_table = np.array([
    #  a_i-1  |alpha_i-1   |  d  | theta
    [    0    ,   0        , d_0 ,  thetas[0]], #1
    [   a_1   ,  alpha_1   , d_1 ,  thetas[1]], #2
    [    0    ,  alpha_2   , d_2 ,  thetas[2]], #3
    [    0    ,  alpha_3   , d_3 ,  thetas[3]], #3
    [    0    ,  alpha_4   , d_4 ,  thetas[4]], #3
    [    0    ,  alpha_5   , d_5 ,  thetas[5]], #3
    [    0    ,  alpha_6   , d_6 ,  thetas[6]], #3
])

P = find_T_total(sawyer_dh_table, print_res=False)[0:3][:,3]

print(P)
# Define cost function

J = 
