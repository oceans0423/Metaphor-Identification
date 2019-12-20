# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:44:32 2019

@author: pcy
"""

import logging
import os.path
import sys
import re
import jieba


# 先用正则将<content>和</content>去掉
def reTest(content):
  reContent = re.sub('<content>|</content>','',content)
  return reContent


f = open('bignews_clean.txt','w+',encoding='utf8')
for line in open('bignews.txt',encoding='utf8'):
    line_clean = reTest(line)
    f.write(line_clean)



