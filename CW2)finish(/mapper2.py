#!/usr/bin/env python
#Answer for mapper.py
import sys
import json
import re

for line in sys.stdin:
    jsonData = json.loads(line.rstrip())        
    try:
        references=jsonData['references']
        page_start=jsonData['page_start']
        page_end=jsonData['page_end']
    except:
         continue
        
    if page_start!="" and page_end!="" and len(page_start)<=6 and page_start.find('-') == -1:
        dictionary=dict()
        dictionary["total_page"]=int(page_end)-int(page_start)+1
        dictionary["total_ref"]=len(references)
            
            
        Output=json.dumps(dictionary)
        print(Output + "\t1") 
