# encoding=utf-8
import codecs

f1 = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
f2 = codecs.open(u'F:\\gddt\\2景点-全面带车站.txt','r','utf-8')
f3 = codecs.open(u'F:\\gddt\\2景点-全面带加油站.txt','r','utf-8')
f4 = codecs.open(u'F:\\gddt\\2景点-全面带停车场.txt','r','utf-8')
f5 = codecs.open(u'F:\\gddt\\5景点-全面-带图片.txt','r','utf-8')
f6 = codecs.open(u'F:\\gddt\\6景点-全面-详细信息.txt','r','utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()
lines3 = f3.readlines()
lines4 = f4.readlines()
lines5 = f5.readlines()
lines6 = f6.readlines()

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()

for i in range(0,50,1):
    id = lines1[i].split('^')[0]
    name = lines1[i].split('^')[1]
    longitude = lines1[i].split('^')[2]
    latitude = lines1[i].split('^')[3]
    
    stations = lines2[i].split('^')[5]
    stations = stations.strip('\r\n')
    stations = stations.replace(',','aaa')
    stations = stations.replace('$','bbb')
    stations = stations.replace('aaa','$')
    stations = stations.replace('bbb','+')
    
    jyz = lines3[i].split('^')[5]
    jyz = jyz.strip('\r\n')
    
    tccs = lines4[i].split('^')[4]
    tccs = tccs.strip('\r\n')
    tccs = tccs.replace('#','aaa')
    tccs = tccs.replace('$','bbb')
    tccs = tccs.replace('aaa','$')
    tccs = tccs.replace('bbb','#')
    
    supporting = stations+"|"+jyz+"|"+tccs
    
    zps = lines5[i].split('^')[5]
    zps = zps.strip('\r\n')
    zps = zps.replace(',','|')
    
    level = lines6[i].split('^')[4]
    addr = lines6[i].split('^')[5]
    
    opentime = lines6[i].split('^')[6]
    jieshao = lines6[i].split('^')[7]
    jieshao = opentime+"|"+jieshao
    
    dianhua = lines6[i].split('^')[8]
    tags = lines6[i].split('^')[9]
    price = lines6[i].split('^')[10]
    price = price.strip('\r\n')
    try:
        price = int(float(price))
    except:
        price = 0
    
    #print id+"^"+name+"^"+longitude+"^"+latitude+"^"+stations+"^"+supporting+"^"+level+"^"+addr+"^"+opentime+"^"+jieshao+"^"+dianhua+"^"+tags+"^"+str(price)
    id1 = lines1[i].split('^')[0]
    id2 = lines2[i].split('^')[0]
    id3 = lines3[i].split('^')[0]
    id4 = lines4[i].split('^')[0]
    id5 = lines5[i].split('^')[0]
    id6 = lines6[i].split('^')[0]
    if not (id1==id2 and id1==id3 and id1==id4 and id1==id5 and id1==id6):
        print id1,id2,id3,id4,id5,id6
        
    #INSERT INTO `xc_tourist` VALUES (default,''ID','姓名','地点','描述',10,'照片','精度','纬度','联系电话','标签','附加');
    ss = "INSERT INTO `xc_tourist` VALUES (default,'%s','%s','%s','%s',%i,'%s','%s','%s','%s','%s','%s');"
    ss = ss %(id,name,addr,jieshao,price,zps,longitude,latitude,dianhua,tags,supporting)
    print ss
    