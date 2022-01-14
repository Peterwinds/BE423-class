import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v0 = 5                    # Initial velocity
g = 9.81                  # Acceleration of gravity
x = linspace(0, 4, 5)  # 1000 points in time interval
y = linspace(0, 4, 5)
A = np.zeros((4, 4))

# At this point, the array y with all the heights is ready.
# Now we need to find the largest value within y.

largest_number = -100000          # Starting value for search
for i in range(4):
    x[i] = i
    for j in range(4):
        y[j] = j
        A[i][j] = (x[i])**2 - (y[j])**2
        if A[i][j] > largest_number:
            largest_number = A[i][j]

print(A)

print ("The largest height achieved was %f m" % (largest_number))

