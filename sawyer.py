import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from kinematics_from_dh import *
from point import Point

try:
    import rospy
except:
    print('\n* rospy did not import. Can only run DH model; cannot run Gazebo sim')

# Python Representation of Sawyer robot
class Sawyer():
    def __init__(self, mode = 'DH'):
        self.mode = mode
        if mode == 'Gazebo':
            print('\n************** Initialized Gazebo model of Sawyer*******************')
            import intera_interface

            # initialize our ROS node, registering it with the Master
            rospy.init_node('Hello_Sawyer')

            # create an instance of intera_interface's Limb class
            self.limb = intera_interface.Limb('right')

            # TODO: Find a way to make this update and easily callable in the form S.angles()
            # Not sure how it interfaces with rostopics, leave for now
            # get the right limb's current joint angles
            self.angles = list(self.limb.joint_angles().values())

            # initialize endpoint position
            self.endpoint = self.limb.endpoint_pose()['position']

            # print the current joint angles
            print("* Initialized at {}".format(str(self.angles)))
        else:
            print('\n*************** Initialized DH model of Sawyer*******************')
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

            self.endpoint = Point(P[0], P[1], P[2])
            # print the current joint angles
            # print("* Initialized at {}".format(str(self.angles)))

    def sleep(self, time):
        if self.mode == 'Gazebo':
            rospy.sleep(time)
        else:
            pass
        
    def move_to_angles(self, thetas, printout = True):
        if self.mode == 'Gazebo':
            angles = {  'right_j0': thetas[0], 
                        'right_j1': thetas[1], 
                        'right_j2': thetas[2],
                        'right_j3': thetas[3], 
                        'right_j4': thetas[4], 
                        'right_j5': thetas[5],
                        'right_j6': thetas[6],
            }
            if printout: print("* Commanding move to {}\n".format(str(thetas)))
            self.limb.move_to_joint_positions(angles)
            self.angles = list(self.limb.joint_angles().values())
            self.endpoint = self.limb.endpoint_pose()['position']
            if printout: print("* Completed move to {}\n".format(str(self.angles)))

        else:
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

            self.endpoint = Point(P[0], P[1], P[2])

            if printout: print("* Completed move to {}\n".format(str(self.angles)))

    def distance_from_target(self, target):
        # Current position
        c = self.endpoint

        # Target position
        t = target

        distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
        
        return distance

    def get_joint_poses(self):
        if self.mode == 'DH':
            prev_T = np.eye(4)
            self.pose_list = []
            for joint in range(1, self.total_joints+1):
                prev_T = np.matmul(prev_T, find_T_i(self.sawyer_dh_table, joint, print_res=False))
                pose = prev_T[0:3][:,3]
                joint_point = Point(pose[0], pose[1], pose[2])
                self.pose_list.append(joint_point)
            return self.pose_list
    
    def plot_sawyer(self):
        if self.mode == 'DH':
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

