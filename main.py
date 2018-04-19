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
TARGET_PATH = "./img/"
ORDER_FETCH_NUM = 99999
KEY_WORD = '武嶺'

#
def checkFolder():
    if not os.path.exists('img'):
        os.makedirs('img')

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
    # print("fetch url:",url)    
    soup = BeautifulSoup(requestPage(url),"html.parser")

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

        if(startAt >= ORDER_FETCH_NUM+200):
            print('fetch end with error')
            break

        if(counter == ORDER_FETCH_NUM):
            print('finish')
            break

