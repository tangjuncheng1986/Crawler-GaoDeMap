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
L1 = range(500101,500121,1)
L3 = ['万州区','涪陵区','渝中区','大渡口区','江北区','沙坪坝区','九龙坡区','南岸区','北碚区','綦江区','大足区','渝北区','巴南区','黔江区','长寿区','江津区','合川区','永川区','南川区','璧山区']
L2 = range(500151,500155,1)
L4 = ['铜梁区','潼南区','荣昌区','开州区']

path = u"F:\\gddt\\1景点-全面.txt"
f1 = codecs.open(path,'a','utf-8')
#for page in range(0,100):
for city in L2:
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
                #print id
                ss = ""
                for allData in allDatas:
                    if isinstance(allData,list):
                        ss = ss+"^"
                    else:
                        ss = ss + allData+"^"
                ss = ss.strip('^')
                if not allDatas[0] in S:
                    #print ss
                    S.add(allDatas[0])
                    f1.write(ss+"\r\n")
        page = page + 1
    #ttt = "\r\n"+str(city)+" "+str(len(S))+"\r\n"
    #print ttt
    #f1.write(ttt)
