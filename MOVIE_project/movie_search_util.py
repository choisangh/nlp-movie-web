import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval

import warnings
warnings.simplefilter('ignore')




#---------------------------------------------------------
# 2. weight ranking based 장르 검색
#---------------------------------------------------------
def my_calc_wr_def(mdf):
    R = mdf['vote_average']
    v = mdf['vote_count']
    WR = (v / (v+m)) * R + (m/ (v+m)) *C
    return WR

def my_search_by_genres(search_genres ='Family', percnet=0.95):
    mldf['wr'] = mldf.apply(my_calc_wr_def, axis=1)
    df5 = mldf[mldf['vote_count'] > m][[ 'id','title', 'genres', 'vote_average', 'vote_count', 'year', 'wr' ]]
    df5 = df5.sort_values('wr', ascending=False)
    print('타입확인', type(df5.loc[0, 'genres']))
    try:
        print('타입확인',type(df5.loc[0,'genres']))
        res = df5[df5['genres'].str.contains(search_genres)]
    except:
        print('타입확인', type(df5.loc[0, 'genres']))
        res = df5[df5['genres'].isin([search_genres])]
    id_list = res['id'].values


    return id_list[:5]

#---------------------------------------------------------
# 3. Review based  리뷰 검색
#---------------------------------------------------------
def my_search_by_review(title = "Toy Story", topn=10):
    s = mldf['title']
    title_s = pd.Series(s.index, index=s.values)  # 값 <--> 인덱스 서로 자리 변경
    title_s = mldf[mldf['title'].str.contains(title, case=False)]['title']
    if len(title_s) > 0:
        idx = title_s[:1].index
    else:
        idx = title_s[title]

    tfidf = TfidfVectorizer(stop_words='english')  # , max_df=0.8, min_df=0.2)  ngram_range=(1, 2)
    tfidf_matrix = tfidf.fit_transform(mldf['view_tag'])
    cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    idx_list = pd.Series(cos_sim[idx].reshape(-1)).sort_values(ascending = False).index[1:topn+1] # 0번재는 본인. 1~10번째
    title_list = mldf.loc[idx_list,'id'].values
    return title_list

#---------------------------------------------------------
# 4. Actor, Driect... based 메타검색
#---------------------------------------------------------
def lambda_get_director_def(s):   #[{'job': 'Director', 'name': 'John Lasseter'} , .... ]
    for dict in s:                #{'job': 'Director', 'name': 'John Lasseter'}
        if dict['job'] == 'Director':
            dict['name'] = dict['name'].replace(' ', '')
            return [dict['name'].lower()]  # [john lasseter]
    return np.nan

def lambda_get_name_def(s):
    cast_list = []
    for dict in s:
        dict['name'] = dict['name'].replace(' ', '')
        cast_list.append(dict['name'].lower())
    return cast_list[:3]

def my_search_by_meta(title = "Toy Story", topn=10):
    try:


        mldf['cast'] = mldf['cast'].apply(literal_eval)  # 배우
        mldf['crew'] = mldf['crew'].apply(literal_eval)  # 감독
        mldf['keywords'] = mldf['keywords'].apply(literal_eval)  # 대표키워드
        mldf['genres2'] = mldf['genres'].apply(literal_eval)  # 장르
    except:
        pass
    mldf['director'] = mldf['crew'].apply(lambda_get_director_def)
    mldf['actor'] = mldf['cast'].apply(lambda_get_name_def)
    mldf['key'] = mldf['keywords'].apply(lambda_get_name_def)
    mldf['search4'] = mldf['director'] + mldf['actor'] + mldf['key'] + mldf['genres2']
    mldf['search4'] = mldf['search4'].astype('str')

    s = mldf['title']
    title_s = pd.Series(s.index, index=s.values)  # 값 <--> 인덱스 서로 자리 변경
    title_s = mldf[mldf['title'].str.contains(title, case=False)]['title']
    if len(title_s) > 0:
        idx = title_s[:1].index
    else:
        idx = title_s[title]

    tfidf = CountVectorizer()  # , max_df=0.8, min_df=0.2)  ngram_range=(1, 2)
    matrix = tfidf.fit_transform(mldf['search4'])
    cos_sim = cosine_similarity(matrix, matrix)
    idx_list = pd.Series(cos_sim[idx].reshape(-1)).sort_values(ascending = False).index[1:topn+1] # 0번재는 본인. 1~10번째
    title_list = mldf.loc[idx_list,'id'].values
    return title_list



mdf = pd.read_csv("./dataset/movies_metadata_2.csv")
ldf = pd.read_csv("./dataset/links_small.csv")
cdf = pd.read_csv("./dataset/credits.csv")
kdf = pd.read_csv("./dataset/keywords.csv")

mdf['id'] = mdf['id'].astype('int')

mldf = pd.merge(mdf, ldf, left_on="id", right_on='tmdbId', how="inner")
mldf = mldf.merge(cdf, on='id')
mldf = mldf.merge(kdf, on='id')  # cast	crew	keywords 추가

mldf['tagline']  = mldf['tagline'].fillna('')
mldf['overview'] = mldf['overview'].fillna('')
mldf['view_tag'] = mldf['overview'] + mldf['tagline']
mldf = mldf.drop(mldf[mldf['view_tag'].str.len() < 1].index, axis=0)
mldf = mldf.reset_index(drop=True)

C = mldf['vote_average'].mean()
m = mldf['vote_count'].quantile(0.95)







