# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle
import logging
from sentence_transformers import SentenceTransformer, InputExample, losses
from scipy.sparse import lil_matrix
from scipy.sparse import hstack

# Load dataset
df_train = pd.read_csv('train_1.csv')
df_test =pd.read_csv('test_ml.tsv', sep='\t')

# Load the SBERT model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Create embeddings
X_train = model.encode(list(df_train.sentence))
X_test = model.encode(list(df_test.sentence))

# Save the embedding results
pickle.dump(X_train, open("/results/train_embeddings_originals.p","wb" ))
pickle.dump(X_test, open("/results/test_embeddings_originals.p", "wb"))

# Optional (w.r.t furthur steps) step to reshape
X_train = np.vstack(X_train)
X_test = np.vstack(X_test)
y_train = df_train["label"]
y_test = df_test["label"]
