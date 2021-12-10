import math
# from typing import Optional

# import gym
# from gym import spaces, logger
# from gym.utils import seeding
# import numpy as np

import rospy
import intera_interface

class SawyerEnv():

    '''
    Description:

    Robotic arm with seven joint angles.
    Range of motion for each: 

    Key rostopics:
    - 

    '''

class Sawyer():
    def __init__(self):
        # initialize our ROS node, registering it with the Master
        rospy.init_node('Hello_Sawyer')

        # create an instance of intera_interface's Limb class
        self.limb = intera_interface.Limb('right')

        # TODO: Find a way to make this update and easily callable in the form S.angles()
        # Not sure how it interfaces with rostopics, leave for now
        # get the right limb's current joint angles
        self.angles = self.limb.joint_angles()

        # initialize endpoint position
        self.endpoint = self.limb.endpoint_pose()['position']

        # print the current joint angles
        print("Initialized at {}".format(str(self.angles)))

    def move2angles(self, angular_array):
        angles = {  'right_j0': angular_array[0], 
                    'right_j1': angular_array[1], 
                    'right_j2': angular_array[2],
                    'right_j3': angular_array[3], 
                    'right_j4': angular_array[4], 
                    'right_j5': angular_array[5],
                    'right_j6': angular_array[6],
        }
        print("Commanding move to {}".format(str(angular_array)))
        self.limb.move_to_joint_positions(angles)
        # self.angles = self.limb.joint_angles()
        # self.endpoint = self.limb.endpoint_pose()['position']
        print("Move complete to {}".format(str(self.limb.joint_angles())))