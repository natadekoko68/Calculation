import numpy as np
import random
import math
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 分子の原子数と次元を定義
num_atoms = 10
dimensions = 3


# ランダムな初期配置を生成
def generate_initial_configuration(num_atoms, dimensions):
    return np.random.rand(num_atoms, dimensions)


# エネルギーを計算する関数（この例では簡単なものとしています）
def calculate_energy(configuration):
    energy = 0.0
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            distance = np.linalg.norm(configuration[i] - configuration[j])
            energy += 1.0 / distance
    return energy


# メインのモンテカルロシミュレーション
def monte_carlo_simulation(num_steps, temperature):
    # 初期配置の生成
    current_configuration = generate_initial_configuration(num_atoms, dimensions)
    current_energy = calculate_energy(current_configuration)

    for step in range(num_steps):
        # ランダムに1つの原子を選択
        random_atom_index = random.randint(0, num_atoms - 1)

        # 原子の位置を少しずらす
        displacement = 0.1 * (np.random.rand(dimensions) - 0.5)
        new_configuration = np.copy(current_configuration)
        new_configuration[random_atom_index] += displacement

        # 新しいエネルギーを計算
        new_energy = calculate_energy(new_configuration)

        # エネルギー差を計算
        delta_energy = new_energy - current_energy

        # メトロポリス条件を適用
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_configuration = new_configuration
            current_energy = new_energy

    return current_configuration, current_energy


# シミュレーションの実行
num_steps = 10000
temperature = 1.0
final_configuration, final_energy = monte_carlo_simulation(num_steps, temperature)

print("Final Configuration:")
print(final_configuration)
print("Final Energy:", final_energy)


def plot_configuration(configuration):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 原子の座標を取得
    x = configuration[:, 0]
    y = configuration[:, 1]
    z = configuration[:, 2]

    ax.scatter(x, y, z, c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Final Molecular Configuration')

    plt.show()


# 分子の原子数と次元を定義
num_atoms = 1000
dimensions = 3


# ランダムな初期配置を生成
def generate_initial_configuration(num_atoms, dimensions):
    return np.random.rand(num_atoms, dimensions)


# エネルギーを計算する関数
def calculate_energy(configuration):
    energy = 0.0
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            distance = np.linalg.norm(configuration[i] - configuration[j])
            energy += 1.0 / distance
    return energy


# メインのモンテカルロシミュレーション
def monte_carlo_simulation(num_steps, temperature):
    current_configuration = generate_initial_configuration(num_atoms, dimensions)
    current_energy = calculate_energy(current_configuration)

    for step in range(num_steps):
        random_atom_index = random.randint(0, num_atoms - 1)
        displacement = 0.1 * (np.random.rand(dimensions) - 0.5)
        new_configuration = np.copy(current_configuration)
        new_configuration[random_atom_index] += displacement
        new_energy = calculate_energy(new_configuration)
        delta_energy = new_energy - current_energy

        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_configuration = new_configuration
            current_energy = new_energy

    return current_configuration, current_energy


# シミュレーションの実行
num_steps = 10000
temperature = 1.0
final_configuration, final_energy = monte_carlo_simulation(num_steps, temperature)

# 結果のプロット
plot_configuration(final_configuration)


