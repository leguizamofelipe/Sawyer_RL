from sawyer_env import *
from intera_interface.limb import Point
import math

S = Sawyer()

endpoint_target = Point(1,1,1)

def distance_from_target(sawyer, target):
    # Current position
    c = sawyer.limb.endpoint_pose()['position']

    # Target position
    t = target

    distance = math.sqrt((c.x-t.x)**2 + (c.y-t.y)**2 + (c.z-t.z)**2)
    
    return distance
    
print(str(distance_from_target(S, endpoint_target)))
