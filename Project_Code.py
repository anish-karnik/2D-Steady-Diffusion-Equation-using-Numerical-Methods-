import numpy as np
import matplotlib.pyplot as plt

l =float(input("Enter value of l1: "))
m=float(input("Enter value of l2: "))
# Number of Grid points
nx = 100
ny = nx
x = np.linspace(0, l, nx)
y = np.linspace(0, m, nx)

dx = x[1] - x[0]
dy = y[1] - y[0]

# k value calculation
k = 2 * ((dx**2 + dy**2) / (dx**2 * dy**2))

# Error and tolerance value
error =10e9
tolerance = 1e-4

# Boundary condition
T_top =float(input("Enter value of Temperature at top:"))
T_left =float(input("Enter value of Temperature at left:"))
T_right = T_left
T_bottom = T_left

T = np.ones((nx, ny))
T[0, :] = T_top
T[-1, :] = T_bottom
T[:, 0] = T_left
T[:, -1] = T_right

# T old value
T_ref = T.copy()

iterations = 1
while error > tolerance:
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            t1 = (T[i + 1, j] + T[i - 1, j]) / (dx ** 2)
            t2 = (T[i, j + 1] + T[i, j - 1]) / (dy ** 2)
            T[i, j] = (t1 + t2) / k

    # Error value calculation
    error = np.max(np.abs(T_ref - T))

    # Updating T_old value
    T_ref = T.copy()

    # Incrementation
    iterations += 1

# Plotting
plt.figure(1)
plt.contourf(x, y, T, cmap='jet', levels=[i for i in range(int(max(T_left,T_top)+1))])
plt.title("Gauss Siedel for 2D Steady Diffusion Equation")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()





