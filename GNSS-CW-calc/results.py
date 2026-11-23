
import numpy as np

normal_position = np.array([
    3956242.02207866,
    -109260.12059223518,
    4985101.631832214
])

scintillation_position = np.array([
    3956222.2879086602,
    -109256.53073905311,
    4985101.428721173
])

difference = scintillation_position - normal_position

error_3d = np.linalg.norm(difference)

print("Coordinate differences (m):", difference)
print(f"3D position difference: {error_3d:.3f} m")
