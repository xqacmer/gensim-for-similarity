from gensim.models import KeyedVectors
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
from scipy.linalg import norm

from nltk.tokenize import word_tokenize
import logging
import os

def vector_similarity(v1,v2):

    return np.dot(v1, v2) / (norm(v1) * norm(v2))
v1 = np.array([0,1,1])
v2 = np.array([0,0,1])
a = vector_similarity(v1,v2)
print(a)