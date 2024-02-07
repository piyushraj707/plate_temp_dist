import numpy as np
import matplotlib.pyplot as plt

# Defining constants
M = 1 # x-direction dimension
N = 2 # y-direction dimension
DEL_X = 0.01 # distance between two grid points in the x-direction
DEL_Y = 0.01 # distance between two grid points in the y-direction
GP_X = int(M/DEL_X) + 1 # The number of Grid Points (GP) in the x-direction
GP_Y = int(N/DEL_Y) + 1 # The number of Grid Points (GP) in the y-direction
T_L = 0 # Temperature on the left surface
T_R = 0 # Temperature on the right surface
T_U = 0 # Temperature on the upper surface
T_B = 100 # Temperature on the bottom surface
ITR = 1000 # Number of interations for Gauss-Seidel Method

T = np.zeros((GP_X, GP_Y)) # T[i][j] = value of temperature at grid location (i, j)

# Defining boundary condition at x=0: Left boundary condition
for j in range(0, GP_Y):
    T[0][j] = T_L

# Defining boundary condition at x=M: Right boundary condition
for j in range(0, GP_Y):
    T[GP_X-1][j] = T_R

# Defining boundary condition at y=0: Bottom boundary condition
for i in range(0, GP_X):
    T[i][0] = T_B

# Defining boundary condition at y=N: Upper boundary condition
for i in range(0, GP_X):
    T[i][GP_Y-1] = T_U

# Applying the Gauss-Seidel iterative method
for _ in range(0, ITR):
    for i in range(1, GP_X-1):
        for j in range(1, GP_Y-1):
            T[i][j] = (DEL_X**(-2)) * T[i+1][j] \
                    + (DEL_X**(-2)) * T[i-1][j] \
                    + (DEL_Y**(-2)) * T[i][j+1] \
                    + (DEL_Y**(-2)) * T[i][j-1]
            T[i][j] /= 2 * ((DEL_X**(-2)) + (DEL_Y**(-2)))


# Plotting the result
plt.imshow(np.rot90(T), cmap='turbo', vmin = min(T_L, T_R, T_U, T_B), vmax = max(T_L, T_R, T_U, T_B))
plt.colorbar()
plt.title("Heat Map for Temperature")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
