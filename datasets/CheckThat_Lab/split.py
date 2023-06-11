import pandas as pd

df = pd.read_table('/content/train_ml.tsv')
df_sample = df.sample(n=6000, random_state=1, replace=False).reset_index(drop=True)
train_1 = df_sample.loc[:2000]
train_2 = df_sample.loc[2001:4000]
train_3 = df_sample.loc[4001:]
train_1.to_csv('train_1.csv', index=False)
train_2.to_csv('train_2.csv', index=False)
train_3.to_csv('train_3.csv', index=False)
