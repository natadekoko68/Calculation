import numpy as np
import matplotlib.pyplot as plt

n_iter = 1000000
step_size = 0.5
x = 0
n_accept = 0

def S(x):
    return 0.5*x**2
def P(x,Z):
    return np.exp(-S(x))/Z

x_history = [0 for i in range(n_iter)]
for i in range(n_iter):
    backup_x = x
    action_init = S(x)
    dx = np.random.rand()
    dx = (dx-0.5)*step_size*2
    x += dx

    action_fin = S(x)

    metropolis = np.random.rand()
    if np.exp(action_init-action_fin) > metropolis:
        n_accept += 1
    else:
        x = backup_x
    x_history[i] = x

# print(x_history)
plt.hist(x_history, bins=300)
# x_lin = np.linspace(-4,4,1000)
# plt.plot(x_lin, P(x_lin,(2*np.pi)**(1/2))*n_iter)
plt.show()