import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import tqdm

n_cities = 10 #都市の数
n_iter = 10000 #繰り返し数
n_m = 1000 #レプリカ数
delta_beta = 0.1 #温度の下げ方

T = [1/((m+1)*delta_beta) for m in range(n_m+1)] #温度

cities = np.random.rand(n_cities, 3) #都市の座標
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
sc = ax1.scatter(cities[:, 0], cities[:, 1], cities[:, 2], marker="+", color="k")
plt.savefig("/Users/kotaro/Desktop/MCMC_3d_init.png", dpi=500)
plt.show()
plt.close()

def calc_dist(i:int, j:int) -> float:
    return ((cities[i][0]-cities[j][0])**2+(cities[i][1]-cities[j][1])**2+(cities[i][2]-cities[j][2])**2)**0.5

#経路のリストから距離を返す関数
def calc_dist_from_path(path: list) -> float:
    dist = 0
    for i in range(len(path)-1):
        dist += calc_dist(path[i], path[i+1])
    dist += calc_dist(path[len(path)-1], path[0])
    return dist

temp_path = [[i for i in range(n_cities)] for _ in range(n_m)]

for iter in tqdm.tqdm(range(n_iter)):
    dists = [0 for i in range(n_m)]
    #レプリカ内に交換操作
    for m in range(n_m):
        dist_init = calc_dist_from_path(temp_path[m])

        k = np.random.randint(0, n_cities-1)
        l = np.random.randint(k+1, n_cities)
        temp_path[m][k], temp_path[m][l] = temp_path[m][l], temp_path[m][k]

        dist_fin = calc_dist_from_path(temp_path[m])

        delta_r = dist_fin - dist_init
        temp_random = np.random.rand()

        if np.random.rand() >= 1-min(1, np.exp(-delta_r/T[m])):
            pass #accepted
        else:
            temp_path[m][k], temp_path[m][l] = temp_path[m][l], temp_path[m][k] #denied
        dists[m] = calc_dist_from_path(temp_path[m])

    #レプリカの交換操作
    for m in range(n_m-1):
        delta_S = (1/T[m+1]-1/T[m])*(dists[m]-dists[m+1])
        if np.random.rand() >= 1 - min(1, np.exp(-delta_S)):
            temp_path[m], temp_path[m+1] = temp_path[m+1], temp_path[m]
        else:
            pass

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
sc = ax1.scatter(cities[:, 0], cities[:, 1], cities[:, 2], marker="+", color="k")
print(cities[:, 0])
x = [cities[temp_path[m][i], 0] for i in range(n_cities)]
y = [cities[temp_path[m][i], 1] for i in range(n_cities)]
z = [cities[temp_path[m][i], 2] for i in range(n_cities)]
line = art3d.Line3D(x,y,z, color='b')
ax1.add_line(line)
ax1.text(x[0], y[0], z[0], "s", color='green')
ax1.text(x[-1], y[-1], z[-1], "g", color='green')

plt.savefig("/Users/kotaro/Desktop/MCMC_3d.png", dpi=500)
plt.show()