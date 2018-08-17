# coding=utf-8
import requests
import json
datas={
    'tid':'556724553832472',
    'num':1,
    'longlife':20
}

def getProxy():
    while True:
        url='http://vtp.daxiangdaili.com/ip'
        r = requests.get(url,params=datas)
        ips = r.text
        ips = ips.split('\r\n')
        ip = ips[0]
        #print ip
        #ip = "http:"
        try:
            res = requests.get('http://www.baidu.com',timeout=10,proxies={'http':ip})
        except:
            continue
        else:
            print 'valid:',ip
            return ip
url = 'http://httpbin.org/ip'
ip = getProxy();
data = requests.get(url,timeout=10).json()
print data
data = requests.get(url,timeout=10,proxies={'http':ip}).json()
print data