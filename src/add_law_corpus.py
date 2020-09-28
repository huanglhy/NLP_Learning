# -*- coding: utf-8 -*-
import re

import jieba

from process import get_stopwords
from read_file import readFromExcel


def prepare_corpus(input_path, output_path):
    output = open(output_path, 'w', encoding="utf-8")
    a = readFromExcel(filepath=input_path)
    a.load_excel()
    for key in a.DataStrut.keys():
        output.writelines(key + '\n')
    for value in a.answerDict.values():
        output.writelines(value + '\n')


def parse_zhwiki(read_file_path, save_file_path):
    # 过滤掉<doc>
    # regex_str = "[^<doc.*>$]|[^</doc>$]"
    file = open(read_file_path, "r", encoding="utf-8")
    # 写文件
    output = open(save_file_path, "w+", encoding="utf-8")
    content_line = file.readline()
    print(len(content_line))
    # 获取停用词表
    stopwords = get_stopwords()
    while content_line:
        words = jieba.cut(content_line, cut_all=False)
        for word in words:
            if word not in stopwords:
                output.write(word + ' ')
        content_line = file.readline()
    output.close()


if __name__ == '__main__':
    # input_path = "../datas/wenshu.xlsx"
    # output_path = '../datas/law/corpus/wenshu_corpus.txt'
    # prepare_corpus(input_path, output_path)
    read_file_path = '../datas/law/corpus/wenshu.txt'
    save_file_path = '../datas/w2v_corpus/wenshu_corpus'
    parse_zhwiki(read_file_path, save_file_path)