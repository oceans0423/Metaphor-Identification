# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:36:27 2019

@author: pcy
"""


import sys
import re
import os
import jieba
import jieba.analyse


f = open('bignews_seg.txt','r+',encoding='utf8')
q = open('news_withtraget酒.txt', 'w+' , encoding='utf8')
for line in open('bignews_seg.txt',encoding='utf8'):
    for word in line:
        if word=='酒':
            q.write(line)
            print(line)
            break

            
count = 1        
for line in open('news_withtraget酒.txt', encoding='utf8'):
    print(count)
    count=count+1

w = open('news_withtraget风.txt', 'w+' , encoding='utf8')
for line in open('bignews_seg.txt',encoding='utf8'):
    for word in line:
        if word=='风':
            w.write(line)
            print(count)
            break

for line in open('news_withtraget风.txt', encoding='utf8'):
    print(count)
    count=count+1

