import itertools as it
from functools import lru_cache
import sys

sys.setrecursionlimit(2000)

@lru_cache(maxsize=100000)
def tarai(x, y, z):
    if x <= y:
        return y
    else:
        return tarai(tarai(x - 1, y, z), tarai(y - 1, z, x), tarai(z - 1, x, y))

def tarai_hypothesis(x,y,z):
    a = min(x,y,z)
    if ((y == a) and (z == a)) or (x==a):
        return y
    elif y == a:
        return z
    elif z == a:
        return max(x, y)

if __name__ == "__main__":
    for i, j, k in it.product(range(1, 101), repeat=3):
        if tarai(i, j, k) != tarai_hypothesis(i, j, k):
            print(i, j, k)