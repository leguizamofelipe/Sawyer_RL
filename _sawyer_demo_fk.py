import numpy as np

from sawyer import *

S = DH_Sawyer()

S.get_joint_poses()
S.move_to_angles([0.5,0.5,0.5,0.5,0.5,0.5,0.5])
S.plot_sawyer()

print(S.endpoint)