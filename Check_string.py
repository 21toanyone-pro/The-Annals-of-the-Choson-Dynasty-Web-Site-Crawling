# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:00:59 2019

@author: DUSK
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import re

#검사할 파일 읽어오기
document_text = open('조선왕조실록(최종편집).txt', 'r', encoding='UTF8' )
text_string = document_text.read()

#사용된 글자 적기
save = open('해당글자.txt', 'w', encoding='utf-8')

data = []
num = 0

bbig = '太'

for i in range(len(text_string)):
    if text_string[i] == bbig:
        #save.write(str(text_string[i+1])+'\n')
        data.append(text_string[i+1])
        data = list(set(data))
        
        
for j in range(len(data)):
    save.write(str(data[j]))
    num +=1
    if num % 10 ==0:
        save.write('\n')
    
save.write('\n총 갯수:'+str(num))