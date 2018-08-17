# coding=utf-8
import requests
import json
from bs4 import BeautifulSoup
import codecs
import time
f = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines = f.readlines()
f.close()
parameter = {
        'cityCode':'500000'
}
baseUrl = 'http://ditu.amap.com/detail/'

f = codecs.open(u'F:\\gddt\\5景点-全面-带图片.txt','w','utf-8')

for line in lines[::1]:
    id = line.split('^')[0]
    url = baseUrl + id
    
    line = line.strip('\r\n')
    line = line + "^"
    
    try:
        r = requests.get(url,params = parameter,timeout=10)
    except:
        time.sleep(10)
        r = requests.get(url,params = parameter,timeout=50)
    cont = r.text
    soup = BeautifulSoup(cont,'html.parser',from_encoding='utf-8')
    try:
        datas = soup.find('div',class_='detail_preview').find('div',class_='display').find('div',class_='display_wrap')
        datas = datas.find('ul').find_all('li')
        for data in datas:
            line = line + data.a['href']+","
        line = line.strip(',')
        line = line+"\r\n"
    except:
        line = line+'\r\n'
    f.write(line)