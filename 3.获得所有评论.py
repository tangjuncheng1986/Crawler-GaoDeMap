# coding=utf-8
import requests
import json
import codecs
url = 'http://ditu.amap.com/detail/get/reviewList'

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

parameter = {
    'poiid':'B001786WBL',
    'pagesize':10,
    'pagenum':1,
    'select_mode':''
}
f = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines = f.readlines()
f.close()
f = codecs.open(u'F:\\gddt\\3景点-全面-评论.txt','w','utf-8')
for line in lines[0:50:1]:
    S = set()
    if line.find('^')==-1:
        f.write(line)
        continue
    line = line.strip('\r\n')
    
    parameter['poiid'] = line.split('^')[0]
    rrr= ""
    for pagenum in range(1,11,1):
        parameter['pagenum'] = pagenum
        r = requests.get(url,params = parameter,headers = headers,timeout=10)
        cont = r.text
        #print r.url
        datas = json.loads(cont)
        datas = datas['data']['review_list']
        flag = True
        for data in datas:
            id = data['review_id']
            if id in S:
                flag = False
            S.add(id)
        if not flag:
            break
            
        for data in datas:
            review = data['review']
            pic = []
            try:
                pics = data['pic_info']
                for p in pics:
                    pic.append(p['url'])
            except:
                pass
            #f.write( review+"\r\n")
            sss = ""
            for p in pic:
                sss = sss + "+" + p
            sss = sss.strip('+')
            review = review + "$" + sss
            review = review.replace('\n','')
            review = review.replace('\r','')
            review = review.replace('^','')
            
            score = data['score']
            time = data['time']
            tt = review+"#"+str(score)+"#"+time
            rrr = rrr + tt+"|"
        if len(datas)<10:
            break
    rrr = rrr.strip('|')
    line = line+rrr+"\r\n"
    f.write(line)
