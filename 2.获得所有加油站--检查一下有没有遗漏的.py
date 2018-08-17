# coding=utf-8
import requests
import json
import codecs
import time

f = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines1 = f.readlines()
f.close()
f = codecs.open(u"F:\\gddt\\2景点-全面带加油站.txt",'r','utf-8')
lines2 = f.readlines()
f.close()

for i in range(0,len(lines2),1):
    id1 = lines1[i].split('^')[0]
    id2 = lines2[i].split('^')[0]
    if id1 != id2:
        print 'error',id1,id2