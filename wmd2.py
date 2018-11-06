from gensim.models import Word2Vec
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
from scipy import spatial
import pandas as pd




def avg_feature_vector(sentence, model, num_features):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    index2word_set = set(model.mv.index2word)
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec



if __name__ =="__main__":
    data = pd.read_csv('data.csv')
    for i in range(9840):
        word1 = data.loc[i]['sentence_A']
        word2 = data.loc[i]['sentence_B']
    print(data.loc[2])