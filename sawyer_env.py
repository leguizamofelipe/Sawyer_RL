import math
import gym
from gym import spaces
import numpy as np
from gym import spaces
import numpy as np

from rospy import sleep
import rospy
import intera_interface

from intera_interface.limb import Point

class SawyerEnv():

    '''
    Description:

    Robotic arm with seven joint angles.
    Range of motion for each: 

    Observation:
        #TODO: Include current state of joints, and inst. vel? in obs space
        Type: float
        Num     Observation               Min                     Max
        0       Distance from target      0                       5000 (infinity)
    
    Actions:
        #TODO: Could restrict motion to subset of joints
        Type: Discrete(2)
        Num   Action
        0     Increase joint 0 pose by +set movement factor
        1     Increase joint 0 pose by -set movement factor
        2     Increase joint 1 pose by +set movement factor
        3     Increase joint 1 pose by -set movement factor
        4     Increase joint 2 pose by +set movement factor
        5     Increase joint 2 pose by -set movement factor
        6     Increase joint 3 pose by +set movement factor
        7     Increase joint 3 pose by -set movement factor
        8     Increase joint 4 pose by +set movement factor
        9     Increase joint 4 pose by -set movement factor
        10    Increase joint 5 pose by +set movement factor
        11    Increase joint 5 pose by -set movement factor
        12    Increase joint 6 pose by +set movement factor
        13    Increase joint 6 pose by -set movement factor

    Reward:
        +1 for every step taken where distance is less than previous distance
        TODO: Function of magnitude of distance delta: getting much closer = higher reward

    Episode Termination:

    '''

class ArmMotionEnvironment():
    """A robot arm motion environment for OpenAI gym"""
    metadata = {'render.modes': ['human']} # TODO understand what this does

    def __init__(self, pos_vec):
        # Initialize Sawyer
        super(ArmMotionEnvironment, self).__init__()

        self.S = Sawyer()

        self.reward_range = (0, 5000) 
        m_f = 0.01

        # Actions: move any of the 7 joints in a +/- movement factor direction
        self.action_space = spaces.Box(low=m_f*np.ones(6), high=m_f*np.ones(6), dtype=int)
        
        # Observations: distance from target; previous distance and current distance
        self.observation_space = spaces.Discrete(2)
    def reset(self):
        # Reset the state of the environment to an initial state (all joints at zero)
        self.angles = np.zeros(6)

        # Set the current robot position randomly
        self.current_step = np.random()
        return self._next_observation()

# Python Representation of Sawyer robot
class Sawyer():
    def __init__(self):
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
	
    class Point():
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
            
    def sleep(self, time):
        rospy.sleep(time)
        
    def move_to_angles(self, angular_array):
        angles = {  'right_j0': angular_array[0], 
                    'right_j1': angular_array[1], 
                    'right_j2': angular_array[2],
                    'right_j3': angular_array[3], 
                    'right_j4': angular_array[4], 
                    'right_j5': angular_array[5],
                    'right_j6': angular_array[6],
        }
        print("* Commanding move to {}\n".format(str(angular_array)))
        self.limb.move_to_joint_positions(angles)
        self.angles = list(self.limb.joint_angles().values())
        self.endpoint = self.limb.endpoint_pose()['position']
        print("* Completed move to {}\n".format(str(self.angles)))

    def distance_from_target(self, target):
        # Current position
        c = self.endpoint

        # Target position
        t = target

        distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
        
        return distance
