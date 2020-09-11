# -*- coding: utf-8 -*-
import json
import logging
import traceback

import jieba
from gensim import models
from gensim.models.wrappers import FastText


from calculate_distance import distCos
from fasttext_vec import law_paragraph
from process import get_stopwords

logger = logging.getLogger(__name__)


def test_text_vec(text):
    print('text预处理')
    # model = models.Word2Vec.load("../model/wiki_corpus00.model")
    # model = FastText.load_fasttext_format("../../../yuanyh/cc.zh.300.bin")
    model = models.Word2Vec.load("../model/law/corpus00.model")
    stopwords = get_stopwords()
    question_contents = []
    words = jieba.cut(text, cut_all=False)
    for word in words:
        if word not in stopwords:
            question_contents.append(word)
    # f = open('../datas/law/unlogin_text.txt', 'w', encoding="utf-8")  # 设置文件对象
    paragraph_vec = law_paragraph(question_contents, model).tolist()
    return paragraph_vec


def similar_law(test_data, test_label):
    '''
        基于聚类模型的预测类别，计算该类别下所有问题与测试数据的余弦相似度
    '''
    # print(test_data, test_label)
    question_label_path = r"../datas/law/question_label_01.json"
    question_path = "../datas/law/question_vec_01.json"
    answer_path = "../datas/law/answer_dict_01.json"
    with open(question_label_path, "r", encoding="utf-8") as question_label_file:
        question_label = json.load(question_label_file)
    with open(question_path, "r", encoding="utf-8") as question_file:
        question_vec = json.load(question_file)
    with open(answer_path, "r", encoding="utf-8") as answer_file:
        answer_dict = json.load(answer_file)
    question_list = question_label.get(str(test_label[0]))
    similar_result = {}
    # print(test_data)
    # print(test_label)
    for question_num in question_list:
        try:
            similar_data = distCos(test_data, question_vec.get(question_num))
            similar_result[question_num] = similar_data
        except Exception as e:
            logger.error(traceback.format_exc())
            # print(question_num)
        # similar_result[question_num] = similar_data
    # 对所求相似度从大到小排序，取前十
    sorted_results = sorted(similar_result.items(), key=lambda item: item[1], reverse=True)[0:10]   # list
    question_order = []
    answer_list = {}
    for sorted_result in sorted_results:
        order = int(sorted_result[0].split('_')[0])
        if order not in question_order:
            question_order.append(order)
            answer_list[answer_dict[str(order)]] = sorted_result[1]
            # answer_list.append(answer_dict[str(order)])
    # print(question_order)
    # print(answer_list)
    return question_order, answer_list











