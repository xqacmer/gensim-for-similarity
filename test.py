from gensim.models import KeyedVectors
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
from scipy.linalg import norm
from scipy import spatial
from nltk.tokenize import word_tokenize
import logging
import os

def avg_feature_vector(sentence, model, num_features, index2word_set):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec

if __name__ =="__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                        level=logging.INFO)

    ExcelFile = xlrd.open_workbook(r'SICK_data.xlsx')
    if os.path.exists(r'new_fileName.xls'):
        os.remove('new_fileName.xls')
    new_excel = copy(ExcelFile)
    # 获取目标EXCEL文件sheet名
    #print(ExcelFile.sheet_names())
    # 制定sheet2
    sheet2_name = ExcelFile.sheet_names()[1]
    ws = new_excel.get_sheet(1)
    # 获取sheet内容【1.根据sheet索引2.根据sheet名称】
    sheet = ExcelFile.sheet_by_name(sheet2_name)
    model = KeyedVectors.load_word2vec_format( fname='GoogleNews-vectors-negative300.bin',binary=True)
    index2word_set = set(model.index2word)
    for i in range(1,9842):
        word1 = sheet.cell(i, 1).value
        word2 = sheet.cell(i, 2).value
        #测试
        # word1 = 'My name is Li min'
        # word2 = 'Her name is Tan ding nan'
        s1_afv = avg_feature_vector(word1, model=model, num_features=300, index2word_set=index2word_set)
        s2_afv = avg_feature_vector(word2, model=model, num_features=300,
                                    index2word_set=index2word_set)
        sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
        print(sim)
        print('--------------------------{}-----------------------'.format(i))

        ws.write(i, 4, sim*5)

    new_excel.save('new_fileName.xls')

