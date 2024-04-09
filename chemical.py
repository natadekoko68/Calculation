import numpy as np
import matplotlib.pyplot as plt

# パラメータ
N = 50  # 分子の数
L = 10.0  # 立方体の一辺の長さ
sigma = 1.0  # Lennard-Jonesポテンシャルのパラメータ
epsilon = 1.0  # Lennard-Jonesポテンシャルのパラメータ
beta = 0.1  # 逆温度
num_steps = 10000  # MCステップ数

# 初期配置の生成
positions = L * np.random.rand(N, 3)


# エネルギー計算
def calculate_energy(positions):
    energy = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            r = np.linalg.norm(positions[i] - positions[j])
            energy += 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)
    return energy


# メトロポリスアルゴリズム
def metropolis(positions, beta):
    new_positions = positions + np.random.uniform(-0.5, 0.5, (N, 3))

    delta_E = calculate_energy(new_positions) - calculate_energy(positions)

    if delta_E < 0 or np.random.rand() < np.exp(-beta * delta_E):
        return new_positions
    else:
        return positions


# モンテカルロシミュレーション
energies = [calculate_energy(positions)]
for step in range(num_steps):
    positions = metropolis(positions, beta)
    energies.append(calculate_energy(positions))

# 結果の表示
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title('Molecule Configuration')
plt.scatter(positions[:, 0], positions[:, 1])
plt.xlim(0, L)
plt.ylim(0, L)
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(2, 1, 2)
plt.title('Energy')
plt.plot(energies)
plt.xlabel('MC Step')
plt.ylabel('Energy')
plt.tight_layout()
plt.show()

