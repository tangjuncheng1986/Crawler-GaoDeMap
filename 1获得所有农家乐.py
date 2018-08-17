# coding=utf-8
import codecs
import JsonUtils
import requests
from bs4 import BeautifulSoup
import time
url = 'http://ditu.amap.com/service/poiInfo'
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'amapuuid':'426876ef-e64e-44cf-806d-5eb7bce4697e',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'guid=15b0-1436-77c3-ab83; UM_distinctid=15d7725d198d3-0171533094c886-871133d-100200-15d7725d19925; passport_login=ODUzMzQ1NzQsYW1hcF8xODgzNTEwOTcwN0NVWFB3ZGdhTCx1cnZ6azB2dGppYnp3azQ4bzRtaGl0aTkwd2xxZmM2bSwxNTAwOTQzMzM0LE9XWTJOelV6WkRFeE9HWmpOV05tTmprMFpERmhZMkZoT0dGbVlUTTBaR1E9; dev_help=%2FHWuUmj%2FOMgDGK3zqxM87GIzNmZmZGE4MzRjNjRhYzA4OTk4MWFhODYxOGI0ODc1MThiN2I5ZmQxZTAzMGRiZmJkZTI4NjBhYTcwODJkODVd%2FpW5grmMh9wV9nFG84oajdDldR%2BRMSwBhxFUI85FBxWk04KKnu8wPwv%2BM5W%2FfKRDPZnskkkkPIjDmZC3tjwMhFBi%2Fl209AXDUkSgO9LSjBTlCzOsxjItBA4UEuBaxgQ%3D; _uab_collina=150094662273412188400085; CNZZDATA1255827602=1821541740-1501129287-http%253A%252F%252Fditu.amap.com%252F%7C1501129287; cna=RIbBEe2XcmECAbe4srSMfpsE; isg=Au_vsn4F6h9d1u4sURMxXD2QfgM5PEPQ9QsI9wF9Ud5oUA9SCWTTBu1ApHYU; key=bfe31f4e0fb231d29e1d3ce951e2c780; CNZZDATA1255626299=235507079-1500945593-http%253A%252F%252Fwww.amap.com%252F%7C1501134671',
    'Host':'ditu.amap.com',
    'Pragma':'no-cache',
    'Referer':'http://ditu.amap.com/search?query=%E5%86%9C%E5%AE%B6%E4%B9%90&city=500000&geoobj=104.652818%7C28.623117%7C109.519761%7C30.921088&zoom=8&pagenum=2',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
parameter = {
    'query_type':'TQUERY',
    'pagesize':20,
    'pagenum':2,
    'qii':'true',
    'cluster_state':5,
    'need_utd':'true',
    'utd_sceneid':1000,
    'div':'PC1000',
    'addr_poi_merge':'true',
    'is_classify':'true',
    'zoom':8,
    'city':500000,
    'geoobj':'104.652818|28.623117|109.519761|30.921088',
    'keywords':'农家乐'
}
'''
http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=2&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=8&city=500000&geoobj=104.652818%7C28.623117%7C109.519761%7C30.921088&keywords=%E5%86%9C%E5%AE%B6%E4%B9%90
'''
path = u"F:\\gddt\\1农家乐.txt"
f1 = codecs.open(path,'w','utf-8')
#for page in range(0,100):
page=1
S= set()
while page<37:
    parameter['pagenum'] = str(page)
    try:
        res = requests.get(url,headers = headers,params=parameter,timeout=10)
    except:
        res = requests.get(url,headers = headers,params=parameter,timeout=50)
    res.encoding='utf-8'
    print res.url
    content = res.text
    datas = JsonUtils.readStr(content)
    try:
        datas = datas['data']['poi_list']
        for data in datas:
            if not data['id'] in S:
                print data['id'],data['name']
                f1.write(data['id']+"^"+data['name']+"^"+data['longitude']+"^"+data['latitude']+"\r\n")
                S.add(data['id'])
    except:
        time.sleep(10)
        page = page - 1
    page = page + 1