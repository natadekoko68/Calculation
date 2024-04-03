import numpy as np
import matplotlib.pyplot as plt
import itertools as it
n_cities = 10

x = np.random.rand(n_cities)
y = np.random.rand(n_cities)

def dist(i, j):
    return ((i[0]-j[0])**2+(i[1]-j[1])**2)**0.5

# for p, q in it.combinations(range(n_cities), 2):
#     print(p,"-",q,":",dist((x[p],y[p]), (x[q],y[q])))


# 全探索
"""
min_len = np.inf
ans = 0

for i in it.permutations(range(n_cities),n_cities):
    temp_len = 0
    for j in range(n_cities-1):
        temp_len += dist((x[i[j]],y[i[j]]), (x[i[j+1]],y[i[j+1]]))
    temp_len += dist((x[i[n_cities-1]], y[i[n_cities-1]]), (x[i[0]], y[i[0]]))
    if temp_len <= min_len:
        min_len = temp_len
        ans = i

for i in range(n_cities-1):
    plt.scatter(x[i], y[i], marker="+", color="k")
    plt.plot((x[ans[i]],x[ans[i+1]]),(y[ans[i]],y[ans[i+1]]), ":", color="black")
plt.scatter(x[n_cities-1], y[n_cities-1], marker="+", color="k")
plt.plot((x[ans[0]],x[ans[n_cities-1]]),(y[ans[0]],y[ans[n_cities-1]]), ":", color="black")
plt.show()
"""

# レプリカ交換法










