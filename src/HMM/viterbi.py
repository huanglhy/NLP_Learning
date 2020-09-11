# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np



def viterbi_algorithm(A, B, pai, O):
    N = np.shape(A)[0]  # 隐马尔科夫模型状态个数
    T = np.shape(O)[0]  # 观测序列的观测个数，即时刻个数
    delta = np.zeros((T, N))  # 每个时刻每个状态对应的局部最优状态序列的概率数组
    psi = np.zeros((T, N))
    #
    pai_0 = pai.reshape(1, len(pai))
    # 计算各个时刻的delta
    for t in range(T):
        if t == 0:
            delta[0] = pai_0 * B[:, O[t]]
            continue
        # print(delta)
        for i in range(N):
            # 对于t时刻每个状态,求最小的
            delta_i_j = delta[t - 1] * A[:, i] * B[i, O[t]]
            delta[t, i] = max(delta_i_j)
            psi[t, i] = np.argmax(delta_i_j)
    print('局部最优状态的概率分布图\n', delta)
    print('局部最优状态的前时刻状态索引图\n', psi)
    t_range = -1 * np.array(sorted(-1 * np.arange(T)))
    states = np.zeros((T,))
    for t in t_range:
        if t == T - 1:
            # 对最后一时刻的状态取值，我们去使得该时刻delta最大的状态
            states[t] = np.argmax(delta[t])
        else:
            # 对任意时刻t，状态的取值为在t+1时刻为
            states[t] = psi[t + 1, int(states[t + 1])]
    print(states)

# 隐马尔可夫模型λ=(A, B, pai)
# A是状态转移概率分布，状态集合Q的大小N=np.shape(A)[0]
# 从下给定A可知：Q={盒1, 盒2, 盒3}, N=3
A = np.array([[0.5, 0.2, 0.3],
              [0.3, 0.5, 0.2],
              [0.2, 0.3, 0.5]])
# B是观测概率分布，观测集合V的大小T=np.shape(B)[1]
# 从下面给定的B可知：V={红，白}，T=2
B = np.array([[0.5, 0.5],
              [0.4, 0.6],
              [0.7, 0.3]])
# pai是初始状态概率分布，初始状态个数=np.shape(pai)[0]
pai = np.array([[0.2],
                [0.4],
                [0.4]])

# O = ['red', 'white', 'red']
O = [0, 1, 0]
def CHMMViterbi():
    # 隐马尔可夫模型λ=(A, B, pai)
    # A是状态转移概率分布，状态集合Q的大小N=np.shape(A)[0]
    # 从下给定A可知：Q={盒1, 盒2, 盒3}, N=3
    A = np.array([[0.5, 0.2, 0.3],
                  [0.3, 0.5, 0.2],
                  [0.2, 0.3, 0.5]])
    # B是观测概率分布，观测集合V的大小T=np.shape(B)[1]
    # 从下面给定的B可知：V={红，白}，T=2
    B = np.array([[0.5, 0.5],
                  [0.4, 0.6],
                  [0.7, 0.3]])
    # pai是初始状态概率分布，初始状态个数=np.shape(pai)[0]
    pai = np.array([[0.2],
                    [0.4],
                    [0.4]])

    # 观测序列
    O = [0, 1, 0]

    viterbi_algorithm(A, B, pai, O)


if __name__ == '__main__':
    CHMMViterbi()

