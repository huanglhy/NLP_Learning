# -*- coding: utf-8 -*-
'''
    改文件用于生成DBSCAN模型
'''
from collections import Counter

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import seaborn as sns
import pandas as pd
# from sklearn.datasets.samples_generator import make_blobs
# from sklearn.preprocessing import StandardScaler

from clustering_algorithm import data_process


def dbscan_algorithm(data):
    print('开始聚类了')
    db = DBSCAN(eps=1, min_samples=5).fit(data)
    data['labels'] = db.labels_
    labels = db.labels_
    # label_count = Counter(labels.tolist())
    print('预测标签：{}'.format(labels))
    print('开始计算分簇数目……')
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print('分簇的数目: %d' % n_clusters_)
    print('开始计算噪声比……')
    raito = len(data.loc[data['labels'] == -1]) / len(data)
    print('噪声比:', format(raito, '.2%'))
    print('开始计算轮廓系数……')
    print("轮廓系数: %0.3f" % metrics.silhouette_score(data, labels))



def parameter_choose(data):
    rs = []
    eps = np.arange(0.2, 4, 0.2)
    min_samples = np.arange(2, 20, 1)
    for i in eps:
        for j in min_samples:
            print('eps={},min_samples={}开始训练'.format(i, j))
            try:
                db = DBSCAN(eps=i, min_samples=j).fit(data)
                labels = db.labels_
                k = metrics.silhouette_score(data, labels, metric='euclidean')
                raito = len(labels[labels[:] == -1]) / len(labels)
                n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
                rs.append([i, j, k, raito, n_clusters_])
            except:
                 db = ''  # 这里用try就是遍历i，j 计算轮廓系数会出错的，出错的就跳过
            else:
                db = ''
    rs = pd.DataFrame(rs)
    rs.columns = ['eps', 'min_samples', 'score', 'raito', 'n_clusters']
    print(rs)
    sns.relplot(x="eps", y="min_samples", size='score', data=rs)
    sns.relplot(x="eps", y="min_samples", size='raito', data=rs)


if __name__ == '__main__':
    question_path = r"../datas/law/question_vec_01.json"
    train_datas, label_list = data_process(question_path)
    train_datas = train_datas.tolist()
    data = pd.DataFrame(train_datas)
    print(len(data))
    # dbscan_algorithm(data)
    parameter_choose(data)