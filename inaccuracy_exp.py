from random import random
from sawyer import *
from point import *
import pickle

S = Sawyer()

active_joints = {   
    0 : {'Max': 1.5, 'Min': 0}, 
    1 : {'Max': 1, 'Min': -1}, 
    2 : {'Max': 3, 'Min': -3},  
    3 : {'Max': 2, 'Min': -2}, 
    4 : {'Max': 2, 'Min': -2}, 
    5 : {'Max': 2, 'Min': -2}, 
    6 : {'Max': 2, 'Min': -2}, 
}

'''
points_dict = {}

for i in range(1, 100): vb
    for joint in active_joints:
        ang.append(active_joints[joint]['Min'] + random() * (active_joints[joint]['Max'] - active_joints[joint]['Min']))

    print(ang)

    points_dict.update({i:ang})

with open('points.p', 'wb') as handle:
    pickle.dump(points_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
'''

with open('points.p', 'rb') as handle:
    points_dict = pickle.load(handle)

for point in points_dict:
    S.move_to_angles(points_dict[point], printout = False)
    print(S.endpoint)
