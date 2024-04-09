path_init = "/Users/kotaro/Desktop/MCMC_3d_init.txt"
path_fin = "/Users/kotaro/Desktop/MCMC_3d.txt"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import numpy as np

cities = []
x = []
y = []
z = []
with open(path_fin) as f:
    for line in f:
        temp_x, temp_y, temp_z = line.rstrip().split()
        x.append(float(temp_x))
        y.append(float(temp_y))
        z.append(float(temp_z))
x = np.array(x)
y = np.array(y)
z = np.array(z)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
sc = ax1.scatter(x, y, z, marker="+", color="k")
line = art3d.Line3D(x, y, z, color='b')
ax1.add_line(line)
ax1.text(x[0], y[0], z[0], "s", color='green')
ax1.text(x[-1], y[-1], z[-1], "g", color='green')

plt.savefig("/Users/kotaro/Desktop/MCMC_3d.png", dpi=500)
plt.show()


