# coding=utf-8
import requests
import json
import time
import codecs
import random

f = codecs.open(u'F:\\gddt\\1景点-全面.txt','r','utf-8')
lines1 = f.readlines()
f.close()
f = codecs.open(u"F:\\gddt\\2景点-全面带停车场.txt",'r','utf-8')
lines2 = f.readlines()
f.close()

for i in range(0,len(lines1),1):
    line1 = lines1[i]
    line2 = lines2[i]
    id1 = line1.split('^')[0]
    id2 = line2.split('^')[0]
    if id1 != id2:
        print 'error',id1,id2