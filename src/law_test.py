# -*- coding: utf-8 -*-
import pickle
import numpy as np

from libs_law import test_text_vec, similar_law


def clustering_test(text):
    test_data_list = test_text_vec(text)
    test_data = np.array(test_data_list)
    test_data.astype(np.float)
    f = open('../model/mykms_01.pickle', 'rb')
    mykms = pickle.load(f)
    f.close()
    result = mykms.predict(test_data.reshape(1, -1))
    question_order, answer_list = similar_law(test_data_list, result)
    print('计算结束')

    return question_order, answer_list


if __name__ == '__main__':
    text = '视频遗嘱的有效条件？'
    question_order, answer_list = clustering_test(text)
    print(question_order, answer_list)

