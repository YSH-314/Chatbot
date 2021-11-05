# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:42:21 2020

@author: NTPU
"""
#產生訓練model
#開啟訓練檔案
from all_deffunction_5 import *
with open("Positive01.txt", "r",encoding='utf-8') as pos:
    positive = pos.read().splitlines()
pos.close()
with open("Negative01.txt", "r",encoding='utf-8') as neg:
    negative = neg.read().splitlines()
neg.close()
with open("stop_words.txt", "r",encoding='utf-8') as st:
    stopwords = st.read().splitlines()
st.close()
  #準備訓練資料
positive_token = remove_sw(positive)
negative_token = remove_sw(negative)
corpus_token = positive_token + negative_token
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer = "word",token_pattern = r"(?u)\b\w+\b") # # 初始化vectorizer, 使用的是bag-of-word 最基礎的 CountVectorizer
word_vectors = vectorizer.fit_transform(corpus_token) # 用這個vectorizer來把我們的corpus編碼
{value : word_vectors.toarray()[:,index] 
                      for index, value in enumerate(vectorizer.get_feature_names())}
import pandas as pd
dataset = pd.DataFrame({value : word_vectors.toarray()[:,index] 
                        for index, value in enumerate(vectorizer.get_feature_names())})
dataset['label']='pos'
dataset.iloc[len(positive_token)+1:,len(vectorizer.get_feature_names())]='neg'
X=dataset.drop(['label'],axis=1)
Y=dataset['label']
  #建立模型
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

  # 實例化(Instantiate) 這個 Naive Bayes Classifier
MNB_model = MultinomialNB()

  # 把資料給它，讓他根據貝氏定理，去算那些機率。
MNB_model.fit(X,Y)
from sklearn.externals import joblib #jbolib模組
#儲存Model(注:save資料夾要預先建立，否則會報錯)
joblib.dump(MNB_model, 'MNB_model.pkl')



