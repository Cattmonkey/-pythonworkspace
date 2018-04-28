# -*- coding: utf-8 -*-
import pandas as pd
import requests

class log:
    def __init__(self, fun):
        self.fun = fun
    def logging(self):
        print(self)
        data = self.fun()
        if 1 == data:
            print("success")
        return data
    


class get_pcs:
    def __enter__(self):
        file= open("out1.csv",'w')
            #with open("out1.csv",'w') as file:
        data = pd.read_csv("in")
        for i in data["phone"]:
            try:
                r=requests.get("http://139.129.204.176:5001/tel_model_juhe?phone="+str(i)).text
            except:
                pass
            di = eval(r)
            line = str(i) + ","+ (str(di.get("juhe2").get("result").get("province"))or str(di.get("juhe2").get("result").get("city")))+ "," + str(di.get("juhe2").get("result").get("company")) + ',' + str(di.get("score"))
            print(line)
            file.write(line+"\n")
        file.close()
        return 
    @log.logging
    def getdata(self):
        file= open("out1.csv",'w')
            #with open("out1.csv",'w') as file:
        data = pd.read_csv("in")
        for i in data["phone"]:
            try:
                r=requests.get("http://139.129.204.176:5001/tel_model_juhe?phone="+str(i)).text
            except:
                pass
            di = eval(r)
            line = str(i) + ","+ (str(di.get("juhe2").get("result").get("province"))or str(di.get("juhe2").get("result").get("city")))+ "," + str(di.get("juhe2").get("result").get("company")) + ',' + str(di.get("score"))
            print(line)
            file.write(line+"\n")
        file.close()
        return 1
       
    def __exit__(self, type, value, trace):
        print("exit")
        return

with get_pcs() as get_message:
    print("ok")
            
        
    