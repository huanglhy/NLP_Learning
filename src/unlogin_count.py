# -*- coding: utf-8 -*-
from collections import defaultdict


def unlogin_count(input_path, output_path):
    input_datas = open(input_path, 'r', encoding='utf-8').readlines()
    output_datas = open(output_path, "w+", encoding="utf-8")
    # f = open('../datas/law/unlogin_text.txt', 'w', encoding="utf-8")  # 设置文件对象

    counts = defaultdict(int)
    # while input_datas:
    for input_data in input_datas:
        counts[input_data] = counts.get(input_data, 0) + 1

    # 对统计结果存储
    for key, value in counts.items():
        txt_data = key.strip('\n') + str(value)
        output_datas.write(txt_data + '\n')



if __name__ == '__main__':
    input_path = '../datas/law/unlogin_words.txt'
    output_path = '../datas/jieba/words_count.txt'
    unlogin_count(input_path, output_path)
