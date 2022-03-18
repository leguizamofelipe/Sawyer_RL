import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from kinematics_from_dh import *

# Python Representation of Sawyer robot
class DH_Sawyer():
    def __init__(self):
        self.angles = [0, 0, 0, 0, 0, 0, 0]
        '''
        # Angle vals in degrees
        self.sawyer_dh_table = np.array([
            #  a_i-1  |alpha_i-1|    d    | theta
            [    0    ,   0    ,   0.317  ,  0 ], #1
            [  0.081  ,  -90   ,   0.191  ,  90], #2
            [    0    ,   90   ,   0.399  ,  0 ], #3
            [    0    ,  -90   ,  -.1683  ,  0 ], #3
            [    0    ,   90   ,   0.3965 ,  0 ], #3
            [    0    ,  -90   ,   0.1360 ,  0 ], #3
            [    0    ,   90   ,  0.1785  ,  0 ], #3
        ])
        '''
        self.sawyer_dh_table = np.array([
            #  a_i-1  |alpha_i-1|      d        | theta
            [    0    ,   0    ,   0.317         ,  0 ], #1
            [  0.081  ,  -90   ,   0.192501      ,  90], #2
            [    0    ,   90   ,   0.4           ,  0 ], #3
            [    0    ,  -90   ,  -.1683         ,  0 ], #3
            [    0    ,   90   ,   0.4           ,  0 ], #3
            [    0    ,  -90   ,   0.1360        ,  0 ], #3
            [    0    ,   90   ,   0.2701        ,  0 ], #3
        ])

        self.total_joints = 7

        # initialize endpoint position
        P = find_T_total(self.sawyer_dh_table, print_res=False)[0:3][:,3]

        self.endpoint = self.Point(P[0], P[1], P[2])
        # print the current joint angles
        # print("* Initialized at {}".format(str(self.angles)))
	
    class Point():
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        def __repr__(self):
            return str(f'{round(self.x,5)},{round(self.y, 5)},{round(self.z, 5)}')

    def sleep(self, time):
        pass
        
    def move_to_angles(self, thetas, printout = True):
        if printout: print("* Commanding move to {}\n".format(str(thetas)))
        self.angles = list(thetas)
        
        self.sawyer_dh_table = np.array([
            #  a_i-1  |alpha_i-1|      d        | theta
            [    0    ,   0    ,   0.317         ,  thetas[0] * 180/3.1415     ], #1
            [  0.081  ,  -90   ,   0.192501      ,  thetas[1] * 180/3.1415 + 90], #2
            [    0    ,   90   ,   0.4           ,  thetas[2] * 180/3.1415     ], #3
            [    0    ,  -90   ,  -.1683         ,  thetas[3] * 180/3.1415     ], #3
            [    0    ,   90   ,   0.4           ,  thetas[4] * 180/3.1415     ], #3
            [    0    ,  -90   ,   0.1360        ,  thetas[5] * 180/3.1415     ], #3
            [    0    ,   90   ,   0.2701        ,  thetas[6] * 180/3.1415     ], #3
        ])

        '''
        self.sawyer_dh_table = np.array([
            #  a_i-1  |alpha_i-1|    d    | theta
            [    0    ,   0    ,     0    ,  thetas[0] * 180/3.1415], 
            [  0.081  ,  -90   ,   0.191  ,  thetas[1] * 180/3.1415], 
            [    0    ,   90   ,   0.399  ,  thetas[2] * 180/3.1415], 
            [    0    ,  -90   ,  -.1683  ,  thetas[3] * 180/3.1415], 
            [    0    ,   90   ,   0.3965 ,  thetas[4] * 180/3.1415], 
            [    0    ,  -90   ,   0.1360 ,  thetas[5] * 180/3.1415], 
            [    0    ,   90   ,   0.1785 ,  thetas[6] * 180/3.1415], 
        ])
        '''
        
        P = find_T_total(self.sawyer_dh_table, print_res=False)[0:3][:,3]

        self.endpoint = self.Point(P[0], P[1], P[2])

        if printout: print("* Completed move to {}\n".format(str(self.angles)))

    def distance_from_target(self, target):
        # Current position
        c = self.endpoint

        # Target position
        t = target

        distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
        
        return distance

    def get_joint_poses(self):
        prev_T = np.eye(4)
        self.pose_list = []
        for joint in range(1, self.total_joints+1):
            prev_T = np.matmul(prev_T, find_T_i(self.sawyer_dh_table, joint, print_res=False))
            pose = prev_T[0:3][:,3]
            joint_point = self.Point(pose[0], pose[1], pose[2])
            self.pose_list.append(joint_point)

        return self.pose_list
    
    def plot_sawyer(self):
        self.get_joint_poses()
        ax = plt.axes(projection = '3d')
        ax.set_xlim([0,1]) # Was 0.5
        ax.set_ylim([0,1]) # Was 0.5
        ax.set_zlim([0,1])
        x_list = [point.x for point in self.pose_list]
        y_list = [point.y for point in self.pose_list]
        z_list = [point.z for point in self.pose_list]
        ax.plot3D(x_list, y_list, z_list, 'blue')
        ax.set_title(f'Endpoint Pose = {self.endpoint}')
        plt.tight_layout()
        plt.show()

