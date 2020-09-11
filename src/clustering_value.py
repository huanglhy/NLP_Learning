# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from clustering_algorithm import data_process
import matplotlib.pyplot as plt


def elbow(n_clusters, train_datas):
    SSE = []
    for i in n_clusters:
        print('{}聚类开始了'.format(i))
        mykms = KMeans(n_clusters=i)
        mykms.fit(train_datas)
        SSE.append(mykms.inertia_)
    print(n_clusters, SSE)
    print('聚类结束，去画手肘了')
    elbow_plot(n_clusters, SSE)


def silhouette_coefficient(n_clusters, train_datas):
    Scores = []  # 存放轮廓系数
    for k in n_clusters:
        print('{}聚类开始了'.format(k))
        estimator = KMeans(n_clusters=k)  # 构造聚类器
        estimator.fit(train_datas)
        Scores.append(silhouette_score(train_datas, estimator.labels_, metric='euclidean'))
    print(n_clusters, Scores)
    plt.xlabel('k')
    plt.ylabel('轮廓系数')
    plt.plot(n_clusters, Scores, 'o-')
    plt.show()


def elbow_silhouette(n_clusters, train_datas):
    SSE = []
    Scores = []  # 存放轮廓系数
    for k in n_clusters:
        print('{}聚类开始了'.format(k))
        estimator = KMeans(n_clusters=k)  # 构造聚类器
        estimator.fit(train_datas)
        SSE.append(estimator.inertia_)
        Scores.append(silhouette_score(train_datas, estimator.labels_, metric='euclidean'))
    print('聚类结束，去画手肘了')
    elbow_plot(n_clusters, SSE)
    print('手肘画完了，去画轮廓系数图了')
    plt.xlabel('k')
    plt.ylabel('轮廓系数')
    plt.plot(n_clusters, Scores, 'o-')
    plt.show()

def elbow_plot(x, y):
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.plot(x, y, 'o-')
    plt.show()



if __name__ == '__main__':
    question_path = r"../datas/law/question_vec_01.json"
    train_datas, label_list = data_process(question_path)
    # n_clusters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # n_clusters = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    n_clusters = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    # elbow(n_clusters, train_datas)
    # silhouette_coefficient(n_clusters, train_datas)
    elbow_silhouette(n_clusters, train_datas)
    # mykms = KMeans(n_clusters=135)
    # y = mykms.fit_predict(train_datas)
    # plot_2D(train_datas, y, 10)