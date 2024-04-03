import numpy as np
import matplotlib.pyplot as plt

n_iter = 10**4
step_size_x = 0.5
step_size_y = 0.5

x = 0
y = 0
n_accept = 0

def S(x,y):
    a = x**2 + y**2 + x * y
    return a/2

record = np.zeros((n_iter,2))

for i in range(n_iter):
    backup_x = x
    backup_y = y

    action_init = S(x,y)

    dx = (np.random.rand() - 0.5) * step_size_x * 2
    dy = (np.random.rand() - 0.5) * step_size_y * 2

    x += dx
    y += dy

    action_fin = S(x,y)

    metropolis = np.random.rand()
    if np.exp(action_init-action_fin) >= metropolis:
        n_accept += 1
    else:
        x = backup_x
        y = backup_y

    record[i][0] = x
    record[i][1] = y

    print(f"{n_accept/n_iter*100:.1f}%")

for j in range(n_iter//10):
    plt.scatter(record[j*10][0], record[j*10][1],marker="+",color="red", alpha=j/1000)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
