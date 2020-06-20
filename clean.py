# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:34:31 2019

@author: DUSK
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import re

def real():
    with open('./광해군정초본.txt', 'r', encoding='UTF8') as file_object:
        contents = file_object.read() #단어 저장

    save = open('광해군정초본_clean2.txt', 'w', encoding='utf-8')
    text = re.sub('{', '', contents)
    text = re.sub('}','',text) #’
    text = re.sub(']','',text)
    text = re.sub('’','',text)
    text = re.sub('「','',text)
    text = re.sub(',','',text)
    text = re.sub(' ','',text)
    text = re.sub('。','',text)
    text = re.sub('〔','',text)
    text = re.sub('〕','',text)
    text = re.sub('、','',text)
    text = re.sub(':','',text)
    text = re.sub('"','',text)
    text = re.sub('/','',text)
    text = re.sub('\n','',text)
    text = re.sub('\t','',text)
    text = re.sub('[?;!‘ㆍ]','',text)
    text = re.sub('[0-9]','',text)
    text = re.sub(r'\【[^)]*\】', '', text)
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\《[^)]*\》', '', text)
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub('[()]','',text)
    #text = list(set(text))

    for i in range(len(text)):
        save.write(str(text[i]))


if __name__ == "__main__":
    real()

    






