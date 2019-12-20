# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:10:24 2019

@author: pcy
"""

import numpy as np
from gensim import corpora,models
import matplotlib.pyplot as plt


model = models.LdaModel.load('lda_wiki_月50.model')
        
#print(model.get_topic_terms(5, topn=10))

        
test = []

index = 0
for line in open('home_poems_seg.txt',encoding='utf8'):
    line = line.strip()
    if not line:
        continue
    word = line.split(' ')
    test.append(word)
    index += 1
print(test)



docs = []
index = 0
for line in open('news_withtraget月new.txt',encoding='utf8'):
    line = line.strip()
    if not line:
        continue
    doc = line.split(' ')
    docs.append(doc)
    index += 1
#print(docs)
       # 构建词典
dictionary = corpora.Dictionary(docs)
bow = [dictionary.doc2bow(word) for word in test]
#print(model.get_document_topics(bow[0],minimum_probability=0.0,minimum_phi_value = 0.0,per_word_topics = False))
for i in range(20):
    poem_topics = model.get_document_topics(bow[i],minimum_probability=0.0,minimum_phi_value = 0.0,per_word_topics = False)
    print(model.get_document_topics(bow[0],minimum_probability=0.0,minimum_phi_value = 0.0,per_word_topics = False))

#poem_topics = model.get_document_topics(bow[i],minimum_probability=0.0,minimum_phi_value = 0.0,per_word_topics = False)
        #print(word_topics)
        
        
    motest1 = np.mat(poem_topics, dtype=float)
    motest2 = np.mat(poem_topics, dtype=int)
            
    y = motest1[:,1]
    x = motest2[:,0]
    print(y)
    print(x)
        
        
    x_axis = np.arange(0, 50,1)
    #xticklabels(x)
    plt.figure(figsize=(12, 6))
    plt.plot(x,y)
    plt.xticks(x_axis)
    xlab = 'topics'
    ylab = 'probability'
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()
          
       


