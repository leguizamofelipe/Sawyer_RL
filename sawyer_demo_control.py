from sawyer_env import *
import math

S = Sawyer()

endpoint_target = S.Point(1,1,1)

# store the first wave position 
wave_1 = [-0.4259, 0.3526, 0.03726, -1.3833, 1.5126, -0.3438, -1.5126]
# store the second wave position
wave_2 = [-0.4281, 0.394, -0.2609, -1.4038, 1.5103, -0.3806, -1.5101]

S.move_to_angles(np.zeros(7))

for wave in range(3):
    S.move_to_angles(wave_1)
    S.sleep(2)
    S.move_to_angles(wave_2)
    S.sleep(2)

print(S.distance_from_target(endpoint_target)) 
