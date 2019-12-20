# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:18:56 2019

@author: pcy
"""
import numpy as np
from gensim import corpora,models
import matplotlib.pyplot as plt

class LDA:
    
    
    def lda_model(self):
        docs = []

        index = 0
        for line in open('news_withtraget月new.txt',encoding='utf8'):
            line = line.strip()
            if not line:
                continue
            doc = line.split(' ')
            docs.append(doc)
            index += 1
        print(docs)
        # 构建词典
        dictionary = corpora.Dictionary(docs)
        # 对文本进行向量化
        corpus = [dictionary.doc2bow(doc) for doc in docs] 
        #tfidf = models.TfidfModel(corpus)
        #corpus_tfidf = tfidf[corpus]
        #print(corpus_tfidf)
        # 使用lda模型进行训练
        lda = models.LdaModel(corpus, id2word = dictionary, num_topics = 70,passes=10)

        # 保存模型
        lda.save('lda_wiki_月70.model')
      # print(lda.print_topics(num_topics=500,num_words=10))
        #lda.
        #corpus_lda = lda[corpus_tfidf]
        #print(len(corpus_lda))
        #for topic in lda.show_topics(num_topics=100):
           # print(topic)
        #for doc in corpus_lda:
         #   print(len(doc))
        #print(lda.get_term_topics('明月',minimum_yprobability = 0.0))
    def test(self):
        model = models.LdaModel.load('lda_wiki_月50.model')
        print(model.print_topics(num_topics=20,num_words=20))
        #print(model.get_topic_terms(5, topn=10))
        
        word_topics = model.get_term_topics('月',minimum_probability=0.0)
        #print(word_topics)
        new_word_topics = []
        j = 0
        for i in range(50):
            if j >= len(word_topics) or word_topics[j][0] != i:
                new_word_topics.append((i, 0))
            else:
                new_word_topics.append(word_topics[j])
                j += 1
        
        print(new_word_topics)
        
        
        motest1 = np.mat(new_word_topics, dtype=float)
        motest2 = np.mat(new_word_topics, dtype=int)
        
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
          
       
    
         
  
        


handler = LDA()
#handler.lda_model()
handler.test()
    