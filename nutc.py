#https://www.google.com/search?q=101&tbm=isch&start=100

import urllib.request
import socket
import re
import sys
import os 
from bs4 import BeautifulSoup 
  
#DEFINE 
TARGET_PATH = "./imgfetch"  #文件保存路徑 
ORDER_FETCH_NUM = 500 #指定擷取數量
MAX_FETCH_NUM = 500 #最大擷取數量

  
def saveFile(path):  
    #檢測當前路徑的有效性  
    if not os.path.isdir(TARGET_PATH):  
        os.mkdir(TARGET_PATH)  
  
    #設置每個圖片的路徑  
    pos = path.rindex('/')  
    t = os.path.join(TARGET_PATH,path[pos+1:])  
    return t  
  
#用if __name__ == '__main__'來判斷是否是在直接運行該.py文件  
  
  
# 網址  
url = "https://www.google.com/search?q=101&tbm=isch&start=100"  
headers = {  
              'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'
           }  
  
req = urllib.request.Request(url=url, headers=headers)  
  
res = urllib.request.urlopen(req)  
  
data = res.read()  

counter = 0

# print(data)

soup = BeautifulSoup(data,"html.parser")

# print(soup.prettify())
print(soup.find_all('img'))
# for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):  
     
#     counter=counter+1    

#     # try:  
#     #     urllib.request.urlretrieve(link,saveFile(link))        
#     # except: 
#     #     counter = counter -1 
#     #     print('fetch fail')
#     #     continue
    
#     print(link,' ',counter,'/500')
    
#     if counter == MAX_FETCH_NUM:
#         break