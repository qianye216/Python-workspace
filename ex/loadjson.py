import json
from time import *
import openpyxl

with open('/Users/raojun/Desktop/get_list.json','r')as f:
    for line in f:
        decodes = json.loads(line)
        a = decodes["data"]["list"]
    for item in a:
        print(item["user_name"])
        # print(item["user_name"].length())
print(ctime())


        
        
    


   



    
