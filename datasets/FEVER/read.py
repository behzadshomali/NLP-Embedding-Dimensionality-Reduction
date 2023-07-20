import pandas as pd
import numpy as np

df_train = pd.read_json('/content/train.jsonl', orient='records', lines=True)
df_train.to_csv('Train.csv', index=False)
Train = pd.read_csv('Train.csv')
print(len(Train)) # 145449


df_test = pd.read_json('/content/shared_task_dev.jsonl', orient='records', lines=True)
df_test.to_csv('Test.csv', index=False)
Test = pd.read_csv('Test.csv')
print(len(Test)) # 19998
