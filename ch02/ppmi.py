import sys
sys.path.append('c:\\Users\\ryosh\\Python\\learn')
import numpy as np
from common.util import preprocess, create_to_matrix, cos_similarity, ppmi

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
C = create_to_matrix(corpus, vocab_size)
W = ppmi(C)

np.set_printoptions(precision=3) # 有効桁
print('covariance matrix')
print(C)
print('-' * 50)
print('PPMI')
print(W)