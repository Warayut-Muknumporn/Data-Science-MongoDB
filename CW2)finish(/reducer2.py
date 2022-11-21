#!/usr/bin/env python
#Answer for reducer.py

import sys
import json
import re
from collections import defaultdict

Sum=[0,0,0,0,0,0,0]
Num=[0,0,0,0,0,0,0]

for row in sys.stdin.readlines():

    key_value_pair = row.split("\t", 1)
    if len(key_value_pair) != 2:
        continue
    articles=json.loads(key_value_pair[0])

    if articles['total_page']>30:
        Sum[6]+=articles['total_ref']
        Num[6]+=1
    elif articles['total_page']<=30 and articles['total_page']>25:
        Sum[5]+=articles['total_ref']
        Num[5]+=1
    elif articles['total_page']<=25 and articles['total_page']>20:
        Sum[4]+=articles['total_ref']
        Num[4]+=1
    elif articles['total_page']<=20 and articles['total_page']>15:
        Sum[3]+=articles['total_ref']
        Num[3]+=1
    elif articles['total_page']<=15 and articles['total_page']>10:
        Sum[2]+=articles['total_ref']
        Num[2]+=1
    elif articles['total_page']<=10 and articles['total_page']>5:
        Sum[1]+=articles['total_ref']
        Num[1]+=1
    elif articles['total_page']<=5 and articles['total_page']>0:
        Sum[0]+=articles['total_ref']
        Num[0]+=1

    
for i in range (len(Num)):   
    if i==0:
        print("1-5\t%s" % str(Sum[0]/Num[0]))
    elif i==1:
        print("6-10\t%s" % str(Sum[1]/Num[1]))
    elif i==2:
        print("11-15\t%s" % str(Sum[2]/Num[2]))
    elif i==3:
        print("16-20\t%s" % str(Sum[3]/Num[3]))
    elif i==4:
        print("21-25\t%s" % str(Sum[4]/Num[4]))
    elif i==5:
        print("26-30\t%s" % str(Sum[5]/Num[5]))
    elif i==6:
        print(">30\t%s" % str(Sum[6]/Num[6]))
