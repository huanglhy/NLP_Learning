# -*- coding: utf-8 -*-
import json
import logging
import traceback
from collections import defaultdict
import numpy as np

import jieba
from gensim import models

from process import get_stopwords
from read_file import readFromExcel
from gensim.models.wrappers import FastText

logger = logging.getLogger(__name__)


def law_paragraph(sentence, model):
    paragraph_1 = []
    for word in sentence:
        try:
            vec = model[word]
            paragraph_1.append(vec)
        except Exception as e:
            logger.error(traceback.format_exc())
            # f.write(word + '\n')
    a = np.array(paragraph_1)
    paragraph_vec = np.mean(a, axis=0)
    return paragraph_vec


def law_vec(input_path, question_path, answer_path):
    a = readFromExcel(filepath=input_path)
    question_output = open(question_path, "w+", encoding="utf-8")
    answer_output = open(answer_path, "w+", encoding="utf-8")
    a.load_excel()
    stopwords = get_stopwords()
    question_dict = defaultdict(list)
    # model = FastText.load_fasttext_format("../../../yuanyh/cc.zh.300.bin")
    model = models.Word2Vec.load("../model/20200928/corpus00.model")
    f = open('../datas/law/unlogin_0810.txt', 'w', encoding="utf-8")  # 设置文件对象
    for key, value in a.DataStrut.items():
        question_contents = []
        words = jieba.cut(key, cut_all=False)
        for word in words:
            if word not in stopwords:
                question_contents.append(word)
        paragraph_vec = law_paragraph(question_contents, model)
        question_dict[value].append(paragraph_vec.tolist())
    question_split = {}
    for key, value in question_dict.items():
        for i in range(len(value)):
            question_split[str(key) + '_' + str(i)] = value[i]
    question_output.write(json.dumps(question_split))
    answer_output.write(json.dumps(a.answerDict))


if __name__ == '__main__':
    input_path = "../datas/questionBase.xls"
    question_path = "../datas/law/question_vec_20200928.json"
    answer_path = "../datas/law/answer_dict_20200928.json"
    law_vec(input_path, question_path, answer_path)
