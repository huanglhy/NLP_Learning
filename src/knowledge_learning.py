# -*- coding: utf-8 -*-
import json
from collections import defaultdict


import jieba
from gensim import models

from process import get_stopwords
from src.read_file import readFromExcel
from calculate_distance import paragraph_vector


def knowledge_vector(input_path, question_path, answer_path):
    '''将每个问题的向量存储'''
    a = readFromExcel(filepath=input_path)
    question_output = open(question_path, "w+", encoding="utf-8")
    # answer_output = open(answer_path, "w+", encoding="utf-8")

    a.load_excel()
    stopwords = get_stopwords()
    question_dict = defaultdict(list)
    model = models.Word2Vec.load("../model/wiki_corpus00.model")
    # answer_dict = {}
    # 使用jieba进行分词
    for key, value in a.DataStrut.items():
        question_contents = []
        words = jieba.cut(key, cut_all=False)
        for word in words:
            if word not in stopwords:
                question_contents.append(word)
        paragraph_vec = paragraph_vector(question_contents, model)
        question_dict[value].append(paragraph_vec.tolist())
    # for key, value in a.answerDict.items():
    #     answer_contents = []
    #     words = jieba.cut(value, cut_all=False)
    #     for word in words:
    #         if word not in stopwords:
    #             answer_contents.append(word)
    #     paragraph_vec = paragraph_vector(answer_contents)
    #     answer_dict[key] = paragraph_vec.tolist()
    # print(question_dict)
    # print(answer_dict)
    question_output.write(json.dumps(question_dict))
    # answer_output.write(json.dumps(answer_dict))

    return question_dict

if __name__ == '__main__':
    intput_path = r'D:\pycharm_project\knowledge_rule\datas\question_ase.xls'
    question_path = r"D:\pycharm_project\knowledge_rule\datas\law\question_vec.json"
    answer_path = r"D:\pycharm_project\knowledge_rule\datas\law\answer_vec.json"
    knowledge_vector(intput_path, question_path, answer_path)







