# coding=utf-8
import requests
import json
import codecs
import time

f1 = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines1 = f1.readlines()
f1.close()

f2 = codecs.open(u'F:\\gddt\\6景点-全面-详细信息.txt','r','utf-8')
lines2 = f2.readlines()
f2.close()

for i in range(0,len(lines2)):
    line1 = lines1[i]
    line2 = lines2[i]
    id1 = line1.split('^')[0]
    id2 = line2.split('^')[0]
    if id1 != id2:
        print i,id1,id2