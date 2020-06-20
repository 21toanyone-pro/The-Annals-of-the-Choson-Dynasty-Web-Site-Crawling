# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:34:31 2019

@author: DUSK
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import re
import clean




def good():
    num =0
    with open('찐.txt', 'r', encoding='UTF8') as file_object:
        contents = file_object.read() #단어 저장

    save = open('없는글자 모음.txt', 'w', encoding='utf-8')

    data = []
    for n in re.findall(r'[\ue0bc-\uefff, \uf100-\uf66e,\uf784-\uf800,\uf806-\uf864,\uf86a-\uf8f7]+', contents):
        data.append(n)
    #\u3400-\u9fff,\u20000-\u2FFFF      # 한자
    #\ue0bc-\uefff, \uf100-\uf66e,\uf784-\uf800,\uf806-\uf864,\uf86a-\uf8f7 # 옛한글
    for i in range(len(data)):
        save.write(str(data[i]))
        num +=1
        if num % 10 ==0:
            save.write('\n')


    with open('없는글자 모음.txt', 'r', encoding='UTF8') as file_object:
        contents2 = file_object.read() #단어 저장
        print(contents2)
    
    save2 = open('옛한글.txt', 'w', encoding='utf-8')
    
    #contents2 = list(set(contents2))
    text = list(set(contents2))

    for i in range(len(contents2)):
        save2.write(str(text[i]))
        #if num % 10 ==0:
        #    save2.write('\n')
    save2.write('\n'+'총:'+str(len(contents2))+'\n')
    clean.real()
    
if __name__ == "__main__":
    good()
    



