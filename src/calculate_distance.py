import re
import jieba
from gensim import models
import numpy as np


# def read_file():
#     zhwiki_path = r"D:\pycharm_project\knowledge_rule\datas\wiki\AA"
#     file_path = zhwiki_path + str("\wiki_00_j")  + '.txt'
#     print(file_path)
#     file = open(file_path, "r", encoding="utf-8")
#     content_line = file.readline()
#     print(content_line)
#     print(len(content_line))
#     regex_str = "[^<doc.*>$]|[^</doc>$]"
#     match_obj = re.match(regex_str, content_line)
#     content_line = content_line.strip("\n")
#     while content_line:
#         match_obj = re.match(regex_str, content_line)
#         content_line = content_line.strip("\n")
#         if len(content_line) > 0:
#             print('111111111111111')
#             if match_obj:
#                 words = jieba.cut(content_line, cut_all=False)
#                 for word in words:
#                     print(word)
#                 print(len(content_line))
#         content_line = file.readline()
#         print(content_line)


# 余弦距离
def distEclud(vecA, vecB):
    diseclud = np.sqrt(np.sum(np.power((vecA - vecB[0]), 2)))
    return diseclud


def distCos(vecA, vecB):

    cos_distance = float(np.sum(np.array(vecA) * np.array(vecB))) / (distEclud(vecA,np.mat(np.zeros(len(vecA)))[0]) * distEclud(vecB,np.mat(np.zeros(len(vecB)))[0]))
    return cos_distance

def paragraph_vector(sentence, model):
    # model = models.Word2Vec.load("../model/wiki_corpus00.model")
    paragraph_1 = []
    for word in sentence:
        if word in model.wv.index2word:
            vec = model[word]
            paragraph_1.append(vec)
        else:
            print(word + '\t\t\t——不在词汇表里' + '\n\n')
    a = np.array(paragraph_1)
    paragraph_vec = np.mean(a, axis=0)
    return paragraph_vec


def sentence_distance(sentence_1, sentence_2):
    # sentence_1 = ['营业厅', '时间', '上班']
    paragraph_vec_1 = paragraph_vector(sentence_1)
    paragraph_vec_2 = paragraph_vector(sentence_2)
    result = distCos(paragraph_vec_1, paragraph_vec_2)
    print(result)
    return result


if __name__ == "__main__":
    sentence_1 = ['今天', '温度', '很', '高']
    sentence_2 = ['今天', '太热']
    sentence_distance(sentence_1, sentence_2)