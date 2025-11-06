
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("final_data.csv",encoding = "cp1252")
data = data.drop(["Unnamed: 0"],axis = 1)

def all_locations():
    return data[~data["cities"].isna()]["cities"].unique()
def all_types():
    return data[~data["type"].isna()]["type"].unique()
def all_industries():
    return data[~data["industry"].isna()]["industry"].unique()

def search(location="all",rating ="all", type_ ="all",industry= "all"):
    res = data.copy(deep = True)
    if  location != "all":
            res= res[res['cities'] == location]
    if rating != "all":
            res = res[res['rating'] == rating]
    if  type_ != "all":
            res = res[res['type'] == type_]
    if industry != "all":
            res = res[res['industry'] == industry]
    return res

def img1(data):
        p1 = data.loc[:,["total_employees","rating"]].groupby("rating").count()
        ind =p1.index
        val = list(map(int,p1.values))
        plt.figure(dpi = 200)
        plt.bar(ind,val,color=["m","c","r","g"])
        ticks = plt.xticks()
        for i in range(len(ticks[0])):
            plt.text(ticks[0][i],val[i],val[i])
        plt.xlabel ("Rating",size = 20)
        plt.ylabel("Count",size = 20)
        plt.savefig("image.png")
        return 

def img2(data):
        p2 = data["old"].apply(lambda x:int(x.split(" ")[1]))
        limit =  (round(p2.max(),-1) )+ 10
        bins = list(range(0,limit+1,10))
        labels = []
        for i in range(0,limit-9,10):
                labels.append(f"{i}-{i+10}")
        p2 = pd.cut(p2,bins,labels=labels)
        p2 = pd.DataFrame({"old":p2.values,"n":np.full(len(p2.values),fill_value = 1 )})  
        p2 = p2.groupby(by = "old").count()
        ind =p2.index
        val = list(map(int,p2.values))
        plt.figure(figsize = (15,4),dpi = 200)
        plt.bar(ind,val,color=["m","c","r","g"])
        ticks = plt.xticks()
        for i in range(len(ticks[0])):
                plt.text(ticks[0][i],val[i],val[i])
        plt.xlabel ("Old",size = 20)
        plt.xticks(rotation = 90)
        plt.ylabel("Count",size = 20)
        plt.savefig("image2.png")
        return

def img3 (data):
      pass

def img4 (data):
      pass

def img5 (data):
      pass

def img6 (data):
      pass
