import pandas as pd
import numpy as np

df_train = pd.read_json('train.json', orient='index')
print(len(df_train)) # 2163

df_test = pd.read_json('test.json', orient='index')
print(len(df_test)) # 638
