# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:10:20 2019

@author: Lim
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os


txt_path = 'C:/Users/DUSK/Desktop/git/Text_Crawling/python/태조_총서/'
outfilename = './text/태조_총서.txt' # 합칠 텍스트

out_file = open(outfilename, 'w', encoding='utf')

files = os.listdir(txt_path)

for filename in files:
    if ".txt" not in filename:
        continue
    file = open(txt_path+filename,encoding='utf')
    for line in file:
        out_file.write(line)
    out_file.write("\n")
    file.close()
out_file.close()