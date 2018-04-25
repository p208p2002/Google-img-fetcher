# IMG-FETCH-WITH-PYTHON v1.0
# Copyright (C) 2018/04/25, Philip Huang

import urllib
import requests
import socket
import re
import sys
import os 
from bs4 import BeautifulSoup 
import datetime
import time
  
# DEFINE 
ORDER_FETCH_NUM = 100
KEY_WORD = '金門'
TARGET_PATH = "./img/"+KEY_WORD

#
def checkFolder():
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)

#
def requestPage(url):    
    headers = {  
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'
            }  
    req = urllib.request.Request(url=url, headers=headers)    
    res = urllib.request.urlopen(req)    
    return res.read()  

# main
checkFolder()
counter = 0
startAt = 0
skip = 20
KEY_WORD = urllib.parse.quote_plus(KEY_WORD)

while(counter<ORDER_FETCH_NUM):    
    url = "https://www.google.com/search?q="+ KEY_WORD +"&source=lnms&tbm=isch&start="+str(startAt)
    startAt = startAt + 20
    print("fetch url:",url)

    try:
        soup = BeautifulSoup(requestPage(url),"html.parser")
    except:
        print('request error')
        continue

    if(counter==0):
        resultStr = soup.find('div',id='resultStats').string
        resultNumStr=''
        for letter in resultStr:
            if( letter == '0' or letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9'):
                resultNumStr = resultNumStr + letter
        
        print('img search result:'+str(resultNumStr))
        print('but google maximum limit at 1000')
        # auto adjust to maximum
        # ORDER_FETCH_NUM = int(resultNumStr)        
        
    
    for link in soup.find_all('img'):       

        counter=counter+1  
        src = link.get('src') 

        try:          
            img_data = requests.get(src).content  
            millis = int(round(time.time()*1000))          
            millis = str(millis)
            with open(os.path.join(TARGET_PATH,'{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())+millis+'.jpg'), 'wb') as handler:
                handler.write(img_data)
                    
        except: 
            counter = counter -1 
            print('fetch fail')
            continue
        
        print(src,' ',counter,'/'+ str(ORDER_FETCH_NUM))

        if(counter >= ORDER_FETCH_NUM):
            print('finish')
            break

