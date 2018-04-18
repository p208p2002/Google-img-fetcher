import urllib.request,socket,re,sys,os  
  
#DEFINE 
TARGET_PATH = "C:\imgfetch"  #文件保存路徑 
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
url = "https://pixabay.com/zh/photos?q=%E5%B1%B1"  
headers = {  
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'  
           }  
  
req = urllib.request.Request(url=url, headers=headers)  
  
res = urllib.request.urlopen(req)  
  
data = res.read()  

counter = 0
for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):  
     
    counter=counter+1    

    # try:  
    #     urllib.request.urlretrieve(link,saveFile(link))        
    # except: 
    #     counter = counter -1 
    #     print('fetch fail')
    #     continue
    
    print(link,' ',counter,'/500')
    
    if counter == MAX_FETCH_NUM:
        break