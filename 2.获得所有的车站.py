# coding=utf-8
import requests
url = 'http://ditu.amap.com/detail/bus/stations'
import json
import codecs
import time
parameter = {
    'longitude':106.996368,
    'latitude':28.885217
}

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'guid=15b0-1436-77c3-ab83; UM_distinctid=15d7725d198d3-0171533094c886-871133d-100200-15d7725d19925; passport_login=ODUzMzQ1NzQsYW1hcF8xODgzNTEwOTcwN0NVWFB3ZGdhTCx1cnZ6azB2dGppYnp3azQ4bzRtaGl0aTkwd2xxZmM2bSwxNTAwOTQzMzM0LE9XWTJOelV6WkRFeE9HWmpOV05tTmprMFpERmhZMkZoT0dGbVlUTTBaR1E9; dev_help=%2FHWuUmj%2FOMgDGK3zqxM87GIzNmZmZGE4MzRjNjRhYzA4OTk4MWFhODYxOGI0ODc1MThiN2I5ZmQxZTAzMGRiZmJkZTI4NjBhYTcwODJkODVd%2FpW5grmMh9wV9nFG84oajdDldR%2BRMSwBhxFUI85FBxWk04KKnu8wPwv%2BM5W%2FfKRDPZnskkkkPIjDmZC3tjwMhFBi%2Fl209AXDUkSgO9LSjBTlCzOsxjItBA4UEuBaxgQ%3D; _uab_collina=150094662273412188400085; cna=RIbBEe2XcmECAbe4srSMfpsE; isg=AiIimfaajwSXEpPXPJQ01xi_c6hE2ybr8JRV7Gy7ThVAP8K5VAN2nai9GU05; CNZZDATA1255626299=235507079-1500945593-http%253A%252F%252Fwww.amap.com%252F%7C1501139140; key=ed8b48166d88845c6fc9b9226fb03277; CNZZDATA1255827602=1821541740-1501129287-http%253A%252F%252Fditu.amap.com%252F%7C1501140087',
    'Host':'ditu.amap.com',
    'Pragma':'no-cache',
    'Referer':'http://ditu.amap.com/detail/B001786WBL?citycode=500000',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

f = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines = f.readlines()
f.close()
f = codecs.open(u"F:\\gddt\\2景点-全面带车站.txt",'w','utf-8')
for line in lines[::]:
    if line.find('^')==-1:
        f.write(line)
        continue
    line = line.strip('\r\n')
    longitude = line.split('^')[2]
    latitude = line.split('^')[3]
    parameter['longitude'] = longitude
    parameter['latitude'] = latitude
    try:
        r = requests.get(url,headers=headers,params=parameter,timeout=10)
    except:
        print 'retrying...'
        time.sleep(10)
        r = requests.get(url,headers=headers,params=parameter,timeout=50)
    r.encoding='utf-8'
    cont = r.text
    datas = json.loads(cont)
    #print r.url
    try:
        res = ""
        datas = datas['data']['busline']
        for data in datas:
            name = data['name']
            distance = data['distance']
            busline = []
            buslines = data['busline']
            for tt in buslines.split('|'):
                busline.append(tt)
            str = ""
            str = name+"$"+distance+"$"+'+'.join(busline)
            res = res + str +"#"
        res = res.strip('#')
        line = line+"^"+res+"\r\n"
    except:
        line = line +"^"+"\r\n"
    #print line
    f.write(line)
f.close()