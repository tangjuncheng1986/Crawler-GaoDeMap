# encoding=utf-8
import codecs

f1 = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
f2 = codecs.open(u'F:\\gddt\\3景点-全面-评论.txt','r','utf-8')


lines1 = f1.readlines()
lines2 = f2.readlines()

f1.close()
f2.close()

f = codecs.open(u'F:\\gddt\\3.txt','w','utf-8')
for i in range(0,50,1):
    id = lines1[i].split('^')[0]
    name = lines1[i].split('^')[1]

    pingluns = lines2[i].split('^')[4]
    if pingluns == "\r\n":
        continue
    for pinglun in pingluns.split('|'):
        wenzi = pinglun.split('#')[0]
        score = pinglun.split('#')[1]
        try:
            score = int(float(score))
        except:
            score = 0
        time = pinglun.split('#')[2]
        time = time.strip("\r\n")
        ss = "INSERT INTO `xc_comment` VALUES (default,'%s',%d,'%s','%s');"
        ss = ss %(id,score,wenzi,time)
        ss = ss + "\r\n"
        f.write(ss)
    id1 = lines1[i].split('^')[0]
    id2 = lines2[i].split('^')[0]
    if not (id1==id2):
        print id1,id2
        
    #INSERT INTO `xc_comment` VALUES (default,'id',5,'评论','日期');

    