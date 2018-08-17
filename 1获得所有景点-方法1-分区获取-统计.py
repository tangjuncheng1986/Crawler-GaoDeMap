# coding=utf-8
import codecs
import JsonUtils
import requests
import time
url = 'http://restapi.amap.com/v3/place/text'
parameter = {
    "key":"e492439ab775ab2aa7e37db054946655",
    #"keywords":"天津",
    "types":"110000",
    "city":500101,
    "citylimit":"true",
    "offset":"20",
    "page":"1",
    "extensions":"all"
}

'''
万州区 96
涪陵区 105
渝中区 174
大渡口区 48
江北区 81
沙坪坝区 178
九龙坡区 132
南岸区 232
北碚区 160
綦江区 164
大足区 94
渝北区 428
巴南区 132
黔江区 72
长寿区 62
江津区 155
合川区 111
永川区 95
南川区 94
璧山区 76

铜梁区 89
潼南区 60
荣昌区 76
开州区 65
'''
L1 = range(500101,500121,1)
L3 = [u'万州区',u'涪陵区',u'渝中区',u'大渡口区',u'江北区',u'沙坪坝区',u'九龙坡区',u'南岸区',u'北碚区',u'綦江区',u'大足区',u'渝北区',u'巴南区',u'黔江区',u'长寿区',u'江津区',u'合川区',u'永川区',u'南川区',u'璧山区']
L2 = range(500151,500155,1)
L4 = [u'铜梁区',u'潼南区',u'荣昌区',u'开州区']

for i in range(0,len(L2),1):
    city = L2[i]
    page=1
    S = set()
    parameter['city']=city
    while True:
        parameter['page'] = str(page)
        try:
            res = requests.get(url,params=parameter,timeout=10)
        except:
            time.sleep(10)
            res = requests.get(url,params=parameter,timeout=50)
        res.encoding='utf-8'
        #print res.url
        content = res.text
        datas = JsonUtils.readStr(content)
        count = datas['count']
        datas = datas['pois']
        if(len(datas)==0):
            print u"爬取结束"
            break
        for data in datas:
            #print data
            try:
                id = data['id']
                names = data['name']
                jwd = data['location']
                allDatas = [id,names,jwd.split(',')[0],jwd.split(',')[1]]
                
            except:
                pass
                print 'error'
            else:
                S.add(id)
        page = page + 1
    print L4[i],len(S)
