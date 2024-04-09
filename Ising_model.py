import numpy as np
import random
import matplotlib.pyplot as plt

# イジングモデルのパラメータ
N = 50  # スピンの数
J = 1.0  # 結合定数
beta = 1.0  # 逆温度

# 初期状態の生成
state = np.random.choice([1, -1], size=N)


# メトロポリスアルゴリズム
def metropolis(state, beta, J):
    for i in range(N):
        # ランダムに選んだスピンのインデックス
        idx = random.randint(0, N - 1)

        # エネルギーの計算
        dE = 2 * J * state[idx] * (state[(idx - 1) % N] + state[(idx + 1) % N])

        # メトロポリス条件
        if dE < 0 or random.random() < np.exp(-beta * dE):
            state[idx] *= -1

    return state


# 交換モンテカルロ法
def exchange_monte_carlo(beta, J, num_exchange=100000):
    states = [state.copy()]  # 初期状態を保存
    energies = [sum(-J * state[i] * state[(i + 1) % N] for i in range(N))]  # 初期エネルギーを保存

    for _ in range(num_exchange):
        new_state = metropolis(state.copy(), beta, J)

        # 交換
        if random.random() < np.exp(
                -beta * (energies[-1] - sum(-J * new_state[i] * new_state[(i + 1) % N] for i in range(N)))):
            state[:] = new_state

        states.append(state.copy())
        energies.append(sum(-J * state[i] * state[(i + 1) % N] for i in range(N)))

    return states, energies


# 交換モンテカルロ法の実行
states, energies = exchange_monte_carlo(beta, J)

# 結果の表示
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title('Spin Configuration')
plt.imshow([states[i] for i in range(0, len(states), 10)], cmap='binary', aspect='auto')
plt.xlabel('Spin Index')
plt.ylabel('MC Step')
plt.colorbar(label='Spin Value')

plt.subplot(2, 1, 2)
plt.title('Energy')
plt.plot(energies)
plt.xlabel('MC Step')
plt.ylabel('Energy')
plt.tight_layout()
plt.show()
