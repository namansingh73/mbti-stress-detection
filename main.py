from wordcloud import STOPWORDS
import pandas as pd
import numpy as np

df = pd.read_csv('mbti_1.csv')


def var_row(row):
    l = []
    for i in row.split('|||'):
        l.append(len(i.split()))
    return np.var(l)


df['words_per_comment'] = df['posts'].apply(lambda x: len(x.split())/50)
df['variance_of_word_counts'] = df['posts'].apply(lambda x: var_row(x))

df.groupby('type').agg({'type': 'count'})

df_2 = df[~df['type'].isin(['ESFJ', 'ESFP', 'ESTJ', 'ESTP'])]
df_2['http_per_comment'] = df_2['posts'].apply(lambda x: x.count('http')/50)
df_2['questionMark_per_comment'] = df_2['posts'].apply(
    lambda x: x.count('?')/50)

print(df_2.groupby('type').agg({'http_per_comment': 'mean'}))
print(df_2.groupby('type').agg({'questionMark_per_comment': 'mean'}))
