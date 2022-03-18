import numpy as np
from math import radians
from math import cos
from math import sin

def find_T_i(dh_table, i, print_res = True):
    a_i_minus_1     = dh_table[i-1, 0]
    alpha_i_minus_1 = radians(dh_table[i-1, 1])
    d_i             = dh_table[i-1, 2]
    theta_i         = radians(dh_table[i-1, 3])

    T = np.array([       
        [        cos(theta_i)                , -sin(theta_i)                              ,          0           , a_i_minus_1                  ],
        [sin(theta_i) * cos(alpha_i_minus_1) ,  cos(theta_i) * cos(alpha_i_minus_1)       , -sin(alpha_i_minus_1), -sin(alpha_i_minus_1) * d_i  ],
        [sin(theta_i) * sin(alpha_i_minus_1) ,  cos(theta_i) * sin(alpha_i_minus_1)       ,  cos(alpha_i_minus_1),  cos(alpha_i_minus_1) * d_i  ],
        [             0                      ,                    0                       ,          0           , 1                            ],
        
    ])

    T = np.around(T, 4)

    if(print_res):
        print(f'************** {i-1}/{i} T = ***********')
        print(T)

    return T

def find_T_total(dh_table, print_res = True, print_intermediate = False):
    r, c = dh_table.shape
    result = np.identity(4)
    for i in range(r):
        result = np.matmul(result, find_T_i(dh_table, i+1, print_intermediate))
    
    if print_res:
        print(f'****************************************')
        print(f'************** {0}/{r} T = ***********')
        print(result)
    
    return result