#!/usr/bin/env python
# coding: utf-8

# In[2]:


from __future__ import division, unicode_literals 
import re


# In[6]:


get_ipython().system('pip install gensim')


# In[11]:


# 불용어 제거
import math
import networkx
import numpy as np
from konlpy import tag as taggers
from collections import Counter
from gensim.corpora import Dictionary, TextCorpus
from gensim.models import TfidfModel
from sklearn.cluster import Birch, DBSCAN, AffinityPropagation
from sklearn.feature_extraction import DictVectorizer

stopwords_ko = ["저", "것", "동시에", "몇", "고려하면", "관련이", "놀라다", "무엇","어느쪽","오","정도의", "더구나", "아무도", "줄은모른다", 
               "참", "아니", "휘익", "향하다", "응당",  "알겠는가", "인젠", "그래서", "자신", "해서는", "둘", "이었다",  "임에", "하도록시키다",
               "누구","이때", "삼", "제외하고", "쿵", "하면", "좀", "그렇지않으면", "아니었다면", "이라면", "팍", "일", "통하여", "무엇때문에",
               "보아", "하게하다", "하는", "이르다", "타다", "까지도", "오직", "도달하다", "잠깐", "외에", "심지어", "하려고하다", "게다가", "후",
               "알", "비하면", "헉헉", "근거로", "월", "따라서", "않는다면", "일지라도", "함께", "이유는", "흥", "혼자", "관하여", "붕붕", "하다",
               "진짜로", "의해", "바와같이", "대하면", "퍽", "보다더", "그렇게", "끼익", "댕그", "시초에", "당장", "하는것만", "누가", "만이",
               "만일", "이지만", "하마터면"]


# In[12]:


get_ipython().system('pip install Article')


# In[6]:


get_ipython().system('pip install newspaper3k')


# In[13]:


from gensim.summarization import summarize
from newspaper import Article
import urllib.request
from bs4 import BeautifulSoup
import time

# url = 'https://sports.news.naver.com/wbaseball/news/read.nhn?oid=477&aid=0000188303''
url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=056&aid=0010709845&date=20190608&type=1&rankingSeq=1&rankingSectionId=105'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
#results = soup.select('h4[class=title]')
results = soup.select("h3[id=articleTitle]")
for result in results:
    title = "기사제목 : " + result.text
    print(title)
    #print("기사제목 : ", result.text)
    print()

news = Article(url, language="ko")
news.download()
news.parse()

summary = summarize(news.text, ratio= 0.2, word_count=70)
print("요약내용")
print(summary)


# In[14]:


## 비교를 위한 네이버 요약봇

애플과 삼성은 스마트 폰에 관한한 영원한 숙적이자 동반자이다.

삼성이 세계 스마트폰 시장을 석권하고 있는 것은 사실이지만 브랜드 가치에서는 애플이 훨씬 앞서고 있다.

최근 미국 경제 전문지 포브스가 세계 200여 개 기업을 대상으로 브랜드 가치를 측정한 결과 
애플이 2,055억 달러, 약 236조 원으로 1위를 차지한 것으로 나타났다.


# In[15]:


# url = 'https://sports.news.naver.com/wbaseball/news/read.nhn?oid=477&aid=0000188303''
url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=056&aid=0010709845&date=20190608&type=1&rankingSeq=1&rankingSectionId=105'
response = urllib.request.urlopen(url)


soup = BeautifulSoup(response, "html.parser")
# #results = soup.select('h4[class=title]')
# results = soup.select("h3[id=articleTitle]")
# for result in results:
#     title = "기사제목 : " + result.text
#     print(title)
#     #print("기사제목 : ", result.text)
#     print()

# news = Article(url, language="ko")
# news.download()
# news.parse()

# summary = summarize(news.text, ratio= 0.2, word_count=70)
# print("요약내용")
# print(summary)


# In[10]:


import json
from collections import OrderedDict

file_data = OrderedDict()


# In[11]:


file_data['title'] = title
file_data['summary'] = summary


# In[12]:


print(json.dumps(file_data, ensure_ascii=False, indent='\t' ))


# In[13]:


with open('samsung.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent='\t')


# In[18]:


print(title)
print()
print(summary)


# In[17]:


pip install pip --upgrade


# In[ ]:




