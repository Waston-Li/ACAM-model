import numpy as np
import  sys

np.set_printoptions(threshold = sys.maxsize)

ent_embed=np.load('../data/'+'music'+'/pretrained_embeddings/ent_embed'+str(50)+'.npy')
ent_movie_test=np.load('../data/'+'movie'+'/data/test'+'.npy')
#print(ent_embed)
print(ent_movie_test)