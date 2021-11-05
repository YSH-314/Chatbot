# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:47:25 2020

@author: NTPU
python 3.6
scikit-learn 0.19.1

在 Anaconda prompt 指令行輸入以下指令：
pip install jieba 
pip install BeautifulSoup4   
pip install html5lib
pip install python-telegram-bot
"""

import jieba
from bs4 import BeautifulSoup
import numpy as np
from tqdm import tqdm 

#從.tx檔讀進python成list
def read_file(file_name):
    try:
      with open(file_name, "r",encoding='utf-8') as line:
        return line.read().splitlines()
      line.close()
    except IOError:
        print('Error: cannot open file')
        
stopwords = read_file("stop_words.txt")

#文字轉成list       
def sentence_list(text):
    text = BeautifulSoup(text, 'html5lib').get_text()#移除html標籤
    sg_list = jieba.cut(text)
    return list(sg_list)

#文字string 去停用字成list
def tokenize(text):
    token_free_words = [word for word in text if word not in "?。」「，.!/;:\n\'\"、@#%^&*"]
    return token_free_words
def remove_noise(tokens):
    noise_free_words = [word for word in tokens if word not in stopwords]
    return noise_free_words
def clean_text(text):
    word_list = sentence_list(text)#轉成單字list
    word_list = tokenize(word_list)#去標點
    word_list = remove_noise(word_list)#去noise
    return word_list


def set_word_vector(word_vecs,dim):
    def word_feature(text,wv=word_vecs,dim=dim):
        emb_cnt = 0
        avg_emb = np.zeros((dim,))

        for word in clean_text(text):

            if word in wv:
                #print(word) 
                avg_emb += wv[word]
                emb_cnt += 1
        avg_emb /= emb_cnt
        return avg_emb
    return word_feature

def euclidean_distance(x, y):   
    return np.sqrt(np.sum((x - y) ** 2))

def cosine_similarity(x, y):
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))
	
# 開啟詞向量檔案
def load_WordVector():
    dim = 0
    word_vecs= {}
    with open("cna.cbow.cwe_p.tar_g.512d.0.txt",encoding="utf-8") as f:
        for line in tqdm(f):
        # 詞向量有512維,由word以及向量中的元素共513個
        # 以空格分隔組成詞向量檔案中一行
            tokens = line.strip().split()

            # txt中的第一列是兩個整數，分別代表有多少個詞以及詞向量維度
            if len(tokens) == 2:
                dim = int(tokens[1])
                continue
            #詞向量從第2列開始
            word = tokens[0] 
            vec = np.array([ float(t) for t in tokens[1:] ])
            word_vecs[word] = vec
    return dim,word_vecs

#.tx檔轉字典 (file1為key；file2為values)
def text_to_dict(file1,file2):
    Q = read_file(file1)
    rejQ = read_file(file2)
    #sentlen = (len(rejQ))-rejQ.count("!")
    
    REBT_dic={}
    c=0
    while "!" in rejQ:
        b=rejQ.index('!')
  
        REBT_dic[Q[c]]=rejQ[0:b]
        c=c+1
        rejQ=rejQ[b+1:]
    return REBT_dic


dim,word_vecs=load_WordVector()
print(len(word_vecs['事件']))
word_feature=set_word_vector(word_vecs,dim)
print(len(word_feature('事件')))


    
def predict(question,answers,debug=False):
    avg_dlg_emb=word_feature(question)
#     print('Question:',question)
    '''if (debug):
        print(clean_text(question))'''

    max_idx = -1
    max_sim = -10
    # 在六個回答中，每個答句都取詞向量平均作為向量表示
    # 我們選出與dialogue句子向量表示cosine similarity最高的短句
    for idx,ans in enumerate(answers):
        avg_ans_emb=word_feature(ans)
        sim = cosine_similarity(avg_dlg_emb,avg_ans_emb)
        #if (debug):
            #print("Ans #%d:%s:" %  (idx,clean_text(ans)))
            #print("Similarity #%d: %f" % (idx, sim))
        if sim > max_sim:
            max_idx = idx
            max_sim = sim
    return answers[max_idx],max_idx,max_sim

#REBT反駁句，input為string
def REBTrej(stringx):
    REBT_dic=text_to_dict('UNRB02.txt','reject02.txt')
    dialogue = stringx
    answers = list(REBT_dic)
    rej = list(REBT_dic.values())
    #print(rej)
    sg_list = jieba.cut(dialogue)

    list(sg_list)
    
    avg_dlg_emb=word_feature(dialogue)

    result = predict(dialogue,answers,debug=True)
#print(result)
    REBT_cat=result[0]
    REBT_idx = result[1]
    #print('類別相似度:',result[2])
    #print('非理性類別:',REBT_cat)
    
    if result[2] <= 0.1:
        return rej[0][0]
    elif result[2] < 0.4:
        return '沒有非理性思考'
    elif result[2] >= 0.4:
    #print('看來你陷入了非理性思考喔，判斷的所屬分類如下:',REBT_cat)
        suggestion = predict(REBT_cat,rej[REBT_idx])
        return suggestion[0]#,suggestion[2]


from sklearn.externals import joblib

#list去停用字成list
def remove_sw(readlist):
    a=[]
    for i in readlist:
        c=[g for g in jieba.cut(i,cut_all=False) if g not in stopwords]
        b=" ".join(c)
        a.append(b)
    return a


positive = read_file("Positive01.txt")
negative = read_file("Negative01.txt")
positive_token = remove_sw(positive)
negative_token = remove_sw(negative)
corpus_token = positive_token + negative_token
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer = "word",token_pattern = r"(?u)\b\w+\b") # # 初始化vectorizer, 使用的是bag-of-word 最基礎的 CountVectorizer
word_vectors = vectorizer.fit_transform(corpus_token)



def encode_text(sentence):
    sr = clean_text(sentence)
    sr = " ".join(sr)
    en_text = vectorizer.transform([sr])
    #print(sr)
    #print(en_text.toarray()[0])
    #print('vector length:', len(en_text.toarray()[0]))
    return en_text

'''def encode_text(sentence):
    readlist=list(sentence)
    sr = remove_sw(readlist)
    s = " ".join(sr)
    #s=' '.join(jieba.cut(sentence,cut_all = True))
    en_text = vectorizer.transform([s])
    #print(en_text.toarray()[0])
    #print('vector length:', len(en_text.toarray()[0]))
    return en_text'''

def PNpredict(model,sentence):
    text=encode_text(sentence)
    return model.predict(text)


#預測正負向情緒，input為string
def PNdis(sentence):    
  #print(model.predict_proba(text))
  #讀取Model
    MNB_model_u = joblib.load('MNB_model.pkl')

    PNresult = PNpredict(MNB_model_u,sentence)

    if PNresult[0]=="pos":
        return 'pos'
    else:
        return 'neg'


#指定對話情境隨機給出回應句，input為key
def randio(S):
  import random
  with open("TAKE_Key.txt", "r",encoding='utf-8') as fd:
      Q = fd.read().splitlines()

  fd.close()

  with open("TAKE_VALUE.txt", "r",encoding='utf-8') as rej:
      rejQ = rej.read().splitlines()
  rej.close()

  REBT_dic={}
  c=0
  while "!" in rejQ:
    b=rejQ.index('!')
  
    REBT_dic[Q[c]]=rejQ[0:b]
    c=c+1
    rejQ=rejQ[b+1:]
  
    
  #print(REBT_dic)
  #print("S1=",REBT_dic['S1'])
  L=len(REBT_dic[S])
  #print("VALUE LEN=",L)
  i=random.randint(0,L-1)  #隨機包含L-1
  #print("ran index=",i)
  rew =   REBT_dic[S][i]
  return rew
  #print(random.choice(list(REBT_dic.values())))





