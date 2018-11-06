from gensim.models import KeyedVectors
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
from scipy.linalg import norm
from nltk.tokenize import word_tokenize
import logging


def vector_similarity(s1, s2):
    def sentence_vector(s):
        words = s.lower().split()
        v = np.zeros(64)
        for word in words:
            v += model[word]
        v /= len(words)
        return v

    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

if __name__ =="__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                        level=logging.INFO)

    ExcelFile = xlrd.open_workbook(r'SICK_data.xlsx')
    new_excel = copy(ExcelFile)
    # 获取目标EXCEL文件sheet名
    print(ExcelFile.sheet_names())
    # 制定sheet2
    sheet2_name = ExcelFile.sheet_names()[1]
    ws = new_excel.get_sheet(1)
    # 获取sheet内容【1.根据sheet索引2.根据sheet名称】
    sheet = ExcelFile.sheet_by_name(sheet2_name)
    model = KeyedVectors.load_word2vec_format( fname='GoogleNews-vectors-negative300.bin',binary=True)

    for i in range(1,5):
        word1 = sheet.cell(i, 1).value
        word2 = sheet.cell(i, 2).value
        #print(word1)
        #print(word2)
        similar = vector_similarity(word1,word2)
        if i <10:
            print(word2,word1,similar)
        ws.write(i, 4, similar*5)
    new_excel.save('new_fileName.xls')
    print(word_tokenize("this's a test"))

