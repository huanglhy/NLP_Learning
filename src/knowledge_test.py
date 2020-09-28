# -*- coding: utf-8 -*-
'''该文件用于测试
    1.读取已有知识向量
    2.提取问题
    3.判断答案准确性

    优化：
    1.考虑相似问题，提高提取问题的概率
    2.添加停用词，将一些不必要的，但是影响距离的词去掉，例如：“问下”'''
import json
import jieba
from gensim import models

from calculate_distance import paragraph_vector, distCos
from process import get_stopwords


def evaluate(question_type, question_paragraph, agent_answer):
    answer_path = r"../datas/knowledge/answer_vec.json"
    question_path = r"../datas/knowledge/question_vec.json"
    model = models.Word2Vec.load("../model/wiki_corpus00.model")
    with open(question_path, "r", encoding="utf-8") as question_file:
        question_vec = json.load(question_file)
    with open(answer_path, "r", encoding="utf-8") as answer_file:
        answer_vec = json.load(answer_file)
    stopwords = get_stopwords()
    question_contents = []
    words = jieba.cut(question_paragraph, cut_all=False)
    for word in words:
        if word not in stopwords:
            question_contents.append(word)
    paragraph_vec = paragraph_vector(question_contents, model)
    for similar_question in question_vec[str(question_type)]:
        question_result = distCos(similar_question, paragraph_vec)
        print('提取到问题的概率: {}'.format(question_result))
        if question_result > 0.6:
            print('命中问题的概率: {}'.format(question_result))
            answer_contents = []
            words = jieba.cut(agent_answer, cut_all=False)
            for word in words:
                if word not in stopwords:
                    answer_contents.append(word)
            answer_paragraph_vec = paragraph_vector(answer_contents, model)
            answer_result = distCos(answer_vec[str(question_type)], answer_paragraph_vec)
            print('坐席回答与标准答案之间的相似度: {}'.format(answer_result))
            if answer_result < 0.9:
                print('命中句子与标准答案之间的相似度: {}'.format(answer_result))
                return answer_result
            break


def test(question_path):
    with open(question_path, "r", encoding="utf-8") as question_file:
        question_vec = json.load(question_file)
    question_split = {}
    for key, value in question_vec.items():
        for i in range(len(value)):
            question_split[key + '_' + str(i)] = value[i]
    print(question_split)


if __name__ == '__main__':
    # evaluate(0, '哦，好的那个营业厅，什么时候上班呢？', '平常周一到周五时间直接去就行。')

    # evaluate(0, '营业厅几点上班？', '周一到周五上午8：00到12:00，下午13:00到17：00。')
    # 上午8：00到12:00，下午13:00到17：00  result = 0.9894472102228844
    # 平常周一到周五时间直接去就行。 result= 0.5749909724914749
    # 周一到周五上午8：00到12:00，下午13:00到17：00。 result= 1
    # 那我就不知道了 result = -0.09225388642671371
    question_path = r"../datas/knowledge/question_vec.json"
    test(question_path)
