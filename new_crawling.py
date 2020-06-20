# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:06:27 2019

@author: DUSK
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Pool, Manager



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


a ='http://sillok.history.go.kr/id/kaa_000001'
b= 'http://sillok.history.go.kr/id/kba_000'
c='http://sillok.history.go.kr/id/kca_000'
d='http://sillok.history.go.kr/id/kda_000'
e='http://sillok.history.go.kr/id/kea_000'
f='http://sillok.history.go.kr/id/kfa_000'
g='http://sillok.history.go.kr/id/wga_000001'

h='http://sillok.history.go.kr/id/kha_10009007_001'
i='http://sillok.history.go.kr/id/kia_10011028_001'
j='http://sillok.history.go.kr/id/kja_10012025_001'
k='http://sillok.history.go.kr/id/kka_10109002_001'
l='http://sillok.history.go.kr/id/kla_10101001_001'
m='http://sillok.history.go.kr/id/kma_10007007_001'
n='http://sillok.history.go.kr/id/kna_10007004_001'
n2='http://sillok.history.go.kr/id/knb_10007003_001'
o='http://sillok.history.go.kr/id/koa_10002001_001'
o2='http://sillok.history.go.kr/id/kob_10002001_001'
p='http://sillok.history.go.kr/id/kpa_10103013_001'
q='http://sillok.history.go.kr/id/kqa_10005008_001'
r='http://sillok.history.go.kr/id/kra_10005004_001'
r2='http://sillok.history.go.kr/id/krb_10005004_001'
s='http://sillok.history.go.kr/id/ksa_10008018_001'
s2='http://sillok.history.go.kr/id/ksb_10008026_001'
t='http://sillok.history.go.kr/id/kta_10006008_001'
t2='http://sillok.history.go.kr/id/ktb_10006008_001'
u='http://sillok.history.go.kr/id/kua_10008030_001'
v='http://sillok.history.go.kr/id/kva_10003010_001'
w='http://sillok.history.go.kr/id/kwa_10007004_001'
x='http://sillok.history.go.kr/id/kxa_10011018_001'
y='http://sillok.history.go.kr/id/kya_10006009_001'
z='http://sillok.history.go.kr/id/kza_10012008_001'
z2='http://sillok.history.go.kr/id/kzb_10007019_001'
z3='http://sillok.history.go.kr/id/kzc_10308029_001'

url = a


driver = webdriver.Chrome('C:\\chromedriver.exe') #위치
driver.implicitly_wait(1) # 로딩 시간

driver.get(url) #조선왕조실록 첫 페이지

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')



Kings = ['태조_총서','정종','태종','세종','문종','단종','세조','예종','성종','연산군','중종','인종','명종','선조','선조수정','광해군중초본','광해군정초본','인조','효종','현종','현종개수',
'숙종','숙종보궐','경종','경종수정','영조','정조','순조','헌종','철종','고종','순종','순종실록부록']
Klink = [a,b,c,d,e,f,g,h,
i,j,k,l,m,n,n2,o,
o2,p,q,r,r2,s,s2,t,
t2,u,v,w,x,y,z,z2,z3]

ii = 0
K_count =0
def get_link(num):

    dir_path = './'+str(Kings[num]) +'/'
    if not os.path.isdir(dir_path):
            os.mkdir(dir_path )  
    save = open(dir_path+str(ii)+'.txt', 'w', encoding='utf')

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    word_moduel = soup.find('div',{'class':'ins_view_in ins_right_in'}).find('div',{'class':'ins_view_pd'}).find_all('p','paragraph') #원문캡처
    for n in word_moduel:
        n.get_text()
        save.write(n.get_text()) 
    return n


while True:
    get_link(K_count)
    old_url = url

    #옆으로 버튼
    driver.find_element_by_xpath('//*[@id="cont_area"]/div[1]/ul[2]/li[2]/a').click()
    url = str(driver.current_url)
    ii = ii+1
    #마지막 페이지 체크
    if old_url == url:
        if K_count >=6:
            break
        else:
            print(Kings[K_count]+'완료')
            K_count = K_count + 1
            ii =0
            url = str(Klink[K_count])
    
 
       










