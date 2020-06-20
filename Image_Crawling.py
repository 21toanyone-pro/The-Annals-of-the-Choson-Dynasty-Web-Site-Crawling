# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:52:08 2019

@author: DUSK
"""

import requests
from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Pool, Manager
import time
from multiprocessing import Pool, Manager
from selenium.webdriver.common.keys import Keys
import pyautogui

Kings = ['태조','정종','태종','세종','문종','단종','세조','예종','성종','연산군','중종','인종','명종','선조','선조수정','광해군중초본','광해군정초본','인조','효종','현종','현종개수',
'숙종','숙종보궐','경종','경종수정','영조','정조','순조','헌종','철종','고종','순종','순종실록부록']
#url = 'http://sillok.history.go.kr/popup/viewer.do?id=kaa'
links = ['kaa','kba','kca','kda','kea','kfa','kga','kha','kia','kja','kka','kla','kma','kna','knb','koa','kob','kpa','kqa','kra','krb','ksa','ksb','kta','ktb','kua',
'kva','kwa','kxa','kya','kza','kzb','kzc']
url = 'http://sillok.history.go.kr/popup/viewer.do?id=' + links[0]#'http://sillok.history.go.kr/popup/viewer.do?id=' + links[3]

options = webdriver.ChromeOptions() 
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\DUSK\Downloads\태조1\1권",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
options.add_argument("disable-gpu")
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome('C:\\chromedriver.exe', chrome_options=options) #위치
driver.implicitly_wait(1) # 로딩 시간
driver.get(url) #조선왕조실록 첫 페이지

html = driver.page_source
soup = bs(html, 'html.parser')
word_moduel = soup.find('div',{'class':'v_loc'}) #태그 검사
ss = word_moduel
i=0
ENTER='/ue007'
#<div class="v_loc" id="title">태조실록/015권/부록/014a면</div>
while True:
    old_ss = ss
    hi=driver.find_element_by_xpath('//*[@id="cont_area"]/div[3]/div[3]/div[3]/ul/li[1]/a').click()
    pyautogui.press('enter')
    hi=driver.find_element_by_xpath('//*[@id="next_ori"]').click() #다음페이지  //*[@id="400256"]/span/a
    html = driver.page_source
    soup = bs(html, 'html.parser')
    new = soup.find('div',{'class':'v_loc'}) #태그 검사
    ss = new
    # if old_ss == ss:
    #     hi=driver.find_element_by_xpath('//*[@id="400254"]/span/a').click()
    #     hi=driver.find_element_by_xpath('//*[@id="400255"]/span/a').click()
    #     hi=driver.find_element_by_xpath('//*[@id="400256"]/span/a').click()
    #     print('wow')
        #break
        # else:
        #     i = i +1
        #     url = 'http://sillok.history.go.kr/popup/viewer.do?id=' + links[i]
        #     driver.get(url) #조선왕조실록 첫 페이지
        #     html = driver.page_source
        #     soup = bs(html, 'html.parser')
            #//*[@id="100175"]/span/a 2
            #//*[@id="100377"]/span/a 3
            

    #print(word_moduel.get_text())


    





