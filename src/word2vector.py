# -*- coding: utf-8 -*-
import multiprocessing

import logging
from gensim.models import word2vec


# def create_model(inp, outp1, outp2, size=200):
#     # LineSentence预处理大文件
#     print("start training the word model")
#     model = Word2Vec(LineSentence(inp), size=size, window=5, min_count=5, workers=multiprocessing.cpu_count())
#     model.save(outp1)
#     model.wv.save_word2vec_format(outp2, binary=False)
#     print("the model have been created")


def word_vec(path):
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)
    # sentences = word2vec.LineSentence(r"D:\pycharm_project\knowledge_rule\datas\wiki\AA\wiki_corpus")
    sentences = word2vec.PathLineSentences(path)
    model = word2vec.Word2Vec(sentences, size=200, window=5, min_count=5, workers=multiprocessing.cpu_count())
    # 保存模型
    model.save("../model/law/corpus00.model")
    # 保存词向量
    model.wv.save_word2vec_format("../model/law/corpus00.vector", binary=False)


if __name__ == "__main__":
    path = '../datas/w2v_corpus'
    word_vec(path)