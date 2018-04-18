#https://www.google.com/search?q=101&tbm=isch&start=100

import urllib.request
import requests
import socket
import re
import sys
import os 
from bs4 import BeautifulSoup 
from PIL import Image
import datetime
  
#DEFINE 
TARGET_PATH = "./img/"  #文件保存路徑 
ORDER_FETCH_NUM = 500 #指定擷取數量
MAX_FETCH_NUM = 500 #最大擷取數量

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
def main():
    checkFolder()
    url = "https://www.google.com/search?q=101&tbm=isch&start=100"       
    soup = BeautifulSoup(requestPage(url),"html.parser")

    counter = 0
    for link in soup.find_all('img'):       
        counter=counter+1  
        src = link.get('src') 

        try:          
            img_data = requests.get(src).content            
            with open(os.path.join(TARGET_PATH,'{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())+'.jpg'), 'wb') as handler:
                handler.write(img_data)
                    
        except: 
            counter = counter -1 
            print('fetch fail')
            continue
        
        print(src,' ',counter,'/500')
        if counter == MAX_FETCH_NUM:
            break

# invoke
main()