# coding=utf-8
import requests
import json
import codecs
import time
url = 'http://restapi.amap.com/v3/place/detail'

parameter = {
    'id':'B001786WBL',
    'output':'json',
    #'key':'e492439ab775ab2aa7e37db054946655',
    'key':'c089302cd8f9fab9fb61170fda8fc0b7'
}
keys = ['e492439ab775ab2aa7e37db054946655','c089302cd8f9fab9fb61170fda8fc0b7','f26762e35183a45be07e7376faf184a8','27c66d12c58a7c82026255cc6c26764b','379cd7253643791d487c8f2f1732dffb','686f375bcee3b59db4e0469ae41dd088','57742040b447ac70e155bc4d589c225d','3626576583d159e80ef35807dbc83154','a15d718c55b48a9cbad40ccdcbcbc046']
f = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines = f.readlines()
f.close()
f = codecs.open(u"F:\\gddt\\6景点-全面-详细信息.txt",'a','utf-8')
validKey = 2
for i in range(1690,len(lines),1):
    line = lines[i]
    parameter['key'] = keys[validKey]
    if line.find('^')==-1:
        f.write(line)
        continue
    line = line.strip('\r\n')
    line = line.strip('^')
    id = line.split('^')[0]
    longitude = line.split('^')[2]
    latitude = line.split('^')[3]
    parameter['id'] = id
    try:
        r = requests.get(url,params = parameter,timeout=10)
    except:
        print 'retrying...'
        time.sleep(10)
        r = requests.get(url,params = parameter,timeout=50)
    cont = r.text
    #print r.url
    try:
        datas = json.loads(cont)
        data = datas['pois'][0]
        #景区的ID
        id = data['id']
        #景区名称 1
        name = data['name']
        #星级 2
        try:
            level = data['deep_info']['level']
        except:#有的deep_info里面没有level的信息
            level = ""
        #所属城市 3
        cityname = data['cityname']
        #所属区 4
        adname = data['adname']
        #详细地址 5
        addr = data['address']
        if not isinstance(addr,list):
            addr = cityname+adname+addr
        else:
            addr = cityname+adname
        #营业时间 6
        try:
            opentime = data['deep_info']['opentime']
        except:
            opentime = ""
        #景点的简介 7
        try:
            intro = data['deep_info']['intro']
        except:
            intro = ""
        #联系电话 11
        tel = data['tel']
        if not isinstance(tel,list):
            tel = tel.replace(";","|")
        #标签 12
        tags=data['type']
        if not isinstance(tags,list):
            tags = tags.replace(';','|')
        #门票 20
        try:
            price = data['deep_info']['price']
        except:
            price = ""
        #经纬度
        jwd = data['location']


        myDatas = [level,addr,opentime,intro,tel,tags,price,cityname,adname]
        #print myDatas
        s = ""
        for myData in myDatas:
            if isinstance(myData,list) or myData is None:
                s = s+"^"+""
            else:
                s = s+"^"+myData
        line = line + s + '\r\n'
        #print line
        f.write(line)
    except:
        validKey = validKey + 1
        if validKey>len(keys)-1:
            print 'no keys,exiting...'
            break
        i = i - 1
    else:
        pass
f.close()