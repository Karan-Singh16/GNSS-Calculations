
import numpy as np


satellites = np.array([
    [10053355.1020386, 15056487.9624351, 25504822.9644244], #sat1
    [20655550.9892971, 5147316.41599376, 16608524.3057565], #sat2
    [21764223.9221401, -6594586.14401236, 15678237.2567117], #sat3
    [10509172.2642949, -14025870.8865179, 25122346.9516909] #sat4
], dtype=float)

# Add the four TEST pseudoranges in satellite order.
norm_pseudoranges = np.array([
    26235692.4410453, #Sat1
    21015824.162323, #Sat2
    21762155.9600294, #Sat3
    25341602.868791 #Sat4
], dtype=float)


receiver = np.zeros(3)
clock_bias = 0.0

for iteration in range(20):

    # Calculate satellite-to-receiver differences
    differences = satellites - receiver

    # Calculate predicted geometric distances
    ranges = np.linalg.norm(differences, axis=1)

    # Calculate pseudorange residuals
    residuals = norm_pseudoranges - (ranges + clock_bias)

    # Construct the 4x4 geometry matrix
    H = np.column_stack((
        -differences / ranges[:, None],
        np.ones(4)
    ))

    # Solve for corrections
    corrections = np.linalg.solve(H, residuals)

    # Update receiver coordinates and clock bias
    receiver = receiver + corrections[:3]
    clock_bias = clock_bias + corrections[3]

    print(f"Iteration {iteration + 1}: {receiver}")

    # Stop when corrections become sufficiently small
    if np.linalg.norm(corrections) < 0.0001:
        break

print("\nFinal ECEF coordinates:")
print("X:", receiver[0])
print("Y:", receiver[1])
print("Z:", receiver[2])
print("Clock bias:", clock_bias)

normal_position = receiver.copy()