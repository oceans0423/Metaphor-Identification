# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:04:13 2019

@author: pcy
"""

import sys
import re
import os
import jieba
import jieba.analyse


#file = open('G:/ciyuanp/LiBaipoems/poems_segmentation.txt','w',encoding='utf-8')



    
#for i in range(len(titles)):
#    print(i, titles[i])

def stopwordslist(stopwords_filepath):  
    stopwords = [line.strip() for line in open(stopwords_filepath, 'r', encoding='utf-8').readlines()]
    stopwords.append('\u3000')
    stopwords.append('\n')
    stopwords.append(' ')
    return stopwords  
 

def segment(userdict_filepath = open("userdict2.txt"), stopwords_filepath = "stopwords.txt"):
    f = open('home_without_stopwords.txt','w+',encoding='utf8')
    jieba.load_userdict(userdict_filepath)
    stopwords = stopwordslist("stopwords.txt") # 这里加载停用词的路径
    for line in open('home_poems.txt',encoding='utf8'):
        seg_list = jieba.cut(line)
        seg_list_without_stopwords = []
        for word in seg_list:
            if word not in stopwords:
                if word !='\t':
                    seg_list_without_stopwords.append(word)
        for word in seg_list_without_stopwords:
            f.write(word)
        f.write('\n')
        
test = segment('userdict2.txt','stopwords.txt')
print(test)
f = open('home_poems_seg.txt','w+',encoding='utf8')    
for line in open('home_without_stopwords.txt',encoding='utf8'):
    seg = jieba.cut(line)
    f.write(' '.join(seg)+'\n')
    
    

    
