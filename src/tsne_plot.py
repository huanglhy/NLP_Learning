# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from clustering_algorithm import data_process

# matplotlib.use('TkAgg')
# from sklearn.manifold import TSNE
#
#
# def plot_embedding(data, label, title, n):
#     fig = plt.figure()
#     ax = plt.subplot(111)
#     color = ['#F0F8FF',
#              '#FAEBD7',
#              '#00FFFF',
#              '#7FFFD4',
#              '#F0FFFF',
#              '#F5F5DC',
#              '#FFE4C4',
#              '#000000',
#              '#FFEBCD',
#              '#0000FF',
#              '#8A2BE2',
#              '#A52A2A',
#              '#DEB887',
#              '#5F9EA0',
#              '#7FFF00',
#              '#D2691E',
#              '#FF7F50',
#              '#6495ED',
#              '#FFF8DC',
#              '#DC143C',
#              '#00FFFF',
#              '#00008B',
#              '#008B8B',
#              '#B8860B',
#              '#A9A9A9',
#              '#006400',
#              '#BDB76B',
#              '#8B008B',
#              '#556B2F',
#              '#FF8C00',
#              '#9932CC',
#              '#8B0000',
#              '#E9967A',
#              '#8FBC8F',
#              '#483D8B',
#              '#2F4F4F',
#              '#00CED1',
#              '#9400D3',
#              '#FF1493',
#              '#00BFFF',
#              '#696969',
#              '#1E90FF',
#              '#B22222',
#              '#FFFAF0',
#              '#228B22',
#              '#FF00FF',
#              '#DCDCDC',
#              '#F8F8FF',
#              '#FFD700',
#              '#DAA520',
#              '#808080',
#              '#008000',
#              '#ADFF2F',
#              '#F0FFF0',
#              '#FF69B4',
#              '#CD5C5C',
#              '#4B0082',
#              '#FFFFF0',
#              '#F0E68C',
#              '#E6E6FA',
#              '#FFF0F5',
#              '#7CFC00',
#              '#FFFACD',
#              '#ADD8E6',
#              '#F08080',
#              '#E0FFFF',
#              '#FAFAD2',
#              '#90EE90',
#              '#D3D3D3',
#              '#FFB6C1',
#              '#FFA07A',
#              '#20B2AA',
#              '#87CEFA',
#              '#778899',
#              '#B0C4DE',
#              '#FFFFE0',
#              '#00FF00',
#              '#32CD32',
#              '#FAF0E6',
#              '#FF00FF',
#              '#800000',
#              '#66CDAA',
#              '#0000CD',
#              '#BA55D3',
#              '#9370DB',
#              '#3CB371',
#              '#7B68EE',
#              '#00FA9A',
#              '#48D1CC',
#              '#C71585',
#              '#191970',
#              '#F5FFFA',
#              '#FFE4E1',
#              '#FFE4B5',
#              '#FFDEAD',
#              '#000080',
#              '#FDF5E6',
#              '#808000',
#              '#6B8E23',
#              '#FFA500',
#              '#FF4500',
#              '#DA70D6',
#              '#EEE8AA',
#              '#98FB98',
#              '#AFEEEE',
#              '#DB7093',
#              '#FFEFD5',
#              '#FFDAB9',
#              '#CD853F',
#              '#FFC0CB',
#              '#DDA0DD',
#              '#B0E0E6',
#              '#800080',
#              '#FF0000',
#              '#BC8F8F',
#              '#4169E1',
#              '#8B4513',
#              '#FA8072',
#              '#FAA460',
#              '#2E8B57',
#              '#FFF5EE',
#              '#A0522D',
#              '#C0C0C0',
#              '#87CEEB',
#              '#6A5ACD',
#              '#708090',
#              '#FFFAFA',
#              '#00FF7F',
#              '#4682B4',
#              '#D2B48C',
#              '#008080',
#              '#D8BFD8',
#              '#FF6347',
#              '#40E0D0',
#              '#EE82EE',
#              '#F5DEB3',
#              '#FFFFFF',
#              '#F5F5F5',
#              '#FFFF00',
#              '#9ACD32']
#     for j in range(n):
#         type_x_j = []
#         type_y_j = []
#         for i in range(data.shape[0]):
#             if label[i] == j:
#                 type_x_j.append(data[i][0])
#                 type_y_j.append(data[i][1])
#         plt.scatter(type_x_j, type_y_j, s=10, c=color[j])
#     plt.xticks()
#     plt.yticks()
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)
#     plt.savefig("../result/{}.jpg".format(n))
#     plt.show()
#
#
# def plot_2D(data, label, epoch):
#     print('Computing t-SNE embedding')
#     tsne = TSNE(n_components=3, init='pca', random_state=0)  # 使用TSNE对特征降到二维
#     print('降维结束')
#     result = tsne.fit_transform(data)  # 降维后的数据
#     # 画图
#     print('要去画图了')
#     fig = plot_embedding(result, label, 't-SNE embedding of the digits (time %.2fs)', 48)
#     fig.subplots_adjust(right=0.8)
#
#
#
# if __name__ == '__main__':
#     question_path = r"../datas/law/question_vec_01.json"
#     train_datas, label_list = data_process(question_path)
#     mykms = KMeans(n_clusters=48)
#     y = mykms.fit_predict(train_datas)
#     plot_2D(train_datas, y, 10)


line = '今天晚上去跑步'
window_size = 3
data = [line[i:] for i in range(window_size)]
print(data)
window_token = list(zip(*data))
print(window_token)