from sawyer_env import *
import math

S = Sawyer()

endpoint_target = S.Point(1,1,1)

# store the first wave position 
wave_1 = [-1.5126, -0.3438, 1.5126, -1.3833, 0.03726, 0.3526, -0.4259]
# store the second wave position
wave_2 = [-1.5101, -0.3806, 1.5103, -1.4038, -0.2609, 0.3940, -0.4281]

S.move_to_angles(wave_1)
S.sleep(2)
S.move_to_angles(wave_2)
S.sleep(2)

print(S.distance_from_target(endpoint_target))
