# -*- coding:utf-8 -*-
'''
        1)已知观测序列
        2)已知模型
        3)求解观测序列概率
'''
import numpy as np


def observation_forward(Q, O, V, A, B, PI ):
    N = len(Q)  # Q状态
    M = len(O)  # O观测
    alphas = np.zeros((N, M))  # 各状态下对应的观测
    T = M
    for t in range(T):
        index_0 = V.index(O[t])
        for i in range(N):
            if t == 0:
                alphas[i][t] = PI[0][i] * B[i][index_0]  # 初始
            else:
                alphas[i][t] = np.dot([alpha[t-1] for alpha in alphas], [a[i] for a in A]) * B[i][index_0]

    P = np.sum([alpha[M-1] for alpha in alphas])
    print('alphas: {}'.format(alphas))
    print('P=%5F' % P)


def observation_backward(Q, O, A, V, B, PI):
    N = len(Q)  # Q状态
    M = len(O)  # O观测
    betas = np.zeros((N, M))  # 各状态下对应的观测
    T = M
    for t in range(T-1, -1, -1):
        for i in range(N):
            if t == T-1:
                betas[i][t] = 1
            else:
                # 三个矩阵相乘
                index_0 = V.index(O[t + 1])
                betas[i][t] = np.sum(np.array(A[i]) * np.array([b[index_0] for b in B]) * np.array([beta[t+1] for beta in betas]))
    P = np.sum(np.array(PI[0]) * np.array([b[V.index(O[0])] for b in B]) * np.array([beta[0] for beta in betas]))
    print('alphas: {}'.format(betas))
    print('P=%5F' % P)


def viterbi(Q, O, V, A, B, PI):
    N = len(Q)  # Q状态
    M = len(O)  # O观测
    T = M
    deltas = np.zeros((N, M))
    psis = np.zeros((N, M))
    I = np.zeros((1, M))
    for t in range(T):
        index_0 = V.index(O[t])
        for i in range(N):
            if t == 0:
                deltas[i][t] = PI[0][i] * B[i][index_0]
                psis[i][t] = 0  
            else:
                deltas[i][t] = max(np.array([delta[t-1] for delta in deltas]) * np.array([a[i] for a in A])) * B[i][index_0]
                psis[i][t] = np.argmax(np.array([delta[t-1] for delta in deltas]) * np.array([a[i] for a in A]))   # * np.array([b[index_0] for b in B])
    I[0][M - 1] = np.argmax([delta[M - 1] for delta in deltas])
    for t in range(M - 2, -1, -1):
        # psis要晚一个时间步，起始将最后那个状态对应在psis那行直接取出就是最后的结果
        # 但是那样体现不出回溯，下面这种每次取上一个最优路径点对应的上一个最优路径点
        I[0][t] = psis[int(I[0][t + 1])][t + 1]
    print(I)
    P = max([delta[T-1] for delta in deltas])
    # pre_Q_T = np.argmax([delta[T-1] for delta in deltas])
    # pre_q = []
    # for t in range(T):
    #     pre_q.append()
    print('deltas: {}'.format(deltas))
    print('psis: {}'.format(psis))
    print('P=%5F' % P)


if __name__ ==  '__main__':
    Q = [1, 2, 3]
    V = ['红', '白']
    A = [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]]
    B = [[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]]
    O = ['红', '白', '红', '白']
    PI = [[0.2, 0.4, 0.4]]
    # observation_forward(Q, O, V, A, B, PI)
    # observation_backward(Q, O, A, V, B, PI)
    viterbi(Q, O, V, A, B, PI)