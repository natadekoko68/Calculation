import numpy as np
import matplotlib.pyplot as plt
import itertools as it;
import tqdm

n_cities = 30 #都市の数
n_iter = 10**4 #繰り返し数
n_m = 200 #レプリカ数
delta_beta = 0.5 #温度の下げ方

T = [1/((m+1)*delta_beta) for m in range(n_m+1)] #温度

cities = np.random.rand(n_cities, 2) #都市の座標

#i番目とj番目の都市間の距離を返す関数
def calc_dist(i:int, j:int) -> float:
    return ((cities[i][0]-cities[j][0])**2+(cities[i][1]-cities[j][1])**2)**0.5

#経路のリストから距離を返す関数
def calc_dist_from_path(path: list) -> float:
    dist = 0
    for i in range(len(path)-1):
        dist += calc_dist(path[i], path[i+1])
    dist += calc_dist(path[len(path)-1], path[0])
    return dist

#レプリカの収容所
temp_path = [[i for i in range(n_cities)] for _ in range(n_m)]

#main()
for iter in tqdm.tqdm(range(n_iter)):
    dists = [0 for i in range(n_m)]
    #レプリカごとに交換操作
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

#グラフの出力
for i in range(len(cities)):
    plt.scatter(*cities[i], marker="+", color="k")
for i in range(n_cities-1):
    plt.plot((cities[temp_path[n_m-1][i]][0],cities[temp_path[n_m-1][i+1]][0]),
             (cities[temp_path[n_m-1][i]][1],cities[temp_path[n_m-1][i+1]][1]),":",color="r")
plt.plot((cities[temp_path[n_m-1][n_cities-1]][0],cities[temp_path[n_m-1][0]][0]),
             (cities[temp_path[n_m-1][n_cities-1]][1],cities[temp_path[n_m-1][0]][1]),":",color="r")
plt.savefig("/Users/kotaro/Desktop/Replica_replace_method.jpg", dpi=300)
plt.show()
