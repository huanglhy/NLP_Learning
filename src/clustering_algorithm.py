# -*- coding: utf-8 -*-
'''该文件用于生成聚类模型'''
import json
import pickle
from collections import defaultdict

import numpy as np

from sklearn.cluster import KMeans


def data_process(question_path):
    with open(question_path, "r", encoding="utf-8") as question_file:
        question_vec = json.load(question_file)
    # 对原始问题和相似问题进行合并，取平均
    # question_vec_mean = defaultdict(list)
    # for key, value in question_vec.items():
    #     i = 0
    #     for data in value:
    #         if isinstance(data, list) and len(data) == 200:
    #             i += 1
    #             continue
    #     if i == len(value):
    #         a = np.array(value)
    #         vec_mean = np.mean(a, axis=0)
    #         question_vec_mean[key] = vec_mean.tolist()
    train_data = []
    # for value in question_vec_mean.values():
    #     if isinstance(value, list) and len(value) == 200:
    #         train_data.append(value)

    # label_dict = defaultdict(int)
    label_list = []
    for key, value in question_vec.items():
        if isinstance(value, list) and len(value) == 200:
            train_data.append(value)
        label_list.append(key)
    train_datas = np.array(train_data)
    return train_datas, label_list


def clustering_model(train_datas, label_list, clusters, question_label_path):
    print('进入聚类了')
    mykms = KMeans(n_clusters=clusters)
    y = mykms.fit_predict(train_datas)
    f = open('../model/mykms_01.pickle', 'wb')
    pickle.dump(mykms, f)
    f.close()
    question_label = open(question_label_path, "w+", encoding="utf-8")
    pre_label = defaultdict(list)
    for i in range(len(y)):
        pre_label[str(y[i])].append(label_list[i])
    question_label.write(json.dumps(pre_label))
    # print(y)
    # print(len(y))
    # return pre_label


if __name__ == '__main__':
    question_path = r"../datas/law/question_vec_01.json"
    question_label_path = r"../datas/law/question_label_01.json"
    train_datas, label_list = data_process(question_path)
    # text = '最低工资标准是多少？'
    # test_vec = [test_text_vec(text)]
    clustering_model(train_datas, label_list, 48, question_label_path)

