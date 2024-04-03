import numpy as np
import matplotlib.pyplot as plt
f = open('/Users/kotaro/Desktop/MCMC6.txt', 'w')

n_iter = 10**7
n_tau = 40
d_tau = 1
def BoxMuller():
    r = np.random.rand()
    s = np.random.rand()

    p = (-2 * np.log(r)) ** 0.5 * np.sin(2 * np.pi * s)
    q = (-2 * np.log(s)) ** 0.5 * np.sin(2 * np.pi * r)

    return p,q

def calc_action(x):
    return 0.5*x**2

def calc_hamiltonian(x,p):
    ham = calc_action(x) + 0.5 * p ** 2
    return ham

def calc_delh(x):
    delh = x
    return delh

def Molecular_Dynamics(x):
    p,q = BoxMuller()
    ham_init = calc_hamiltonian(x, p)
    x += p * 0.5 * d_tau
    for i in range(1, n_tau):
        del_h = calc_delh(x)
        p -= del_h*d_tau
        x += p * d_tau
    del_h = calc_delh(x)
    p -= del_h*d_tau
    x += p * d_tau * 0.5

    ham_fin = calc_hamiltonian(x,p)
    return x,ham_init, ham_fin

x = 0
n_accept = 0
sum_xx = 0
record = np.zeros(n_iter)

for i in range(n_iter):
    backup_x = x
    x, ham_init, ham_fin = Molecular_Dynamics(x)
    metropolis = np.random.rand()
    if np.exp(ham_init - ham_fin) > metropolis:
        n_accept += 1
    else:
        x = backup_x
    record[i] = x

    sum_xx += x ** 2
    f.write(f"\n=={i+1}回目==\n-{sum_xx/(i+1):.6f}\n-{n_accept/(i+1)*100:.4f}%\n")

plt.hist(record, bins=300)
plt.savefig("/Users/kotaro/Desktop/MCMC6.png", dpi=300)
plt.show()

f.close()


