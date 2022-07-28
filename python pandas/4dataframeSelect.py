import random
import pandas as pd
import numpy as np

#3*3 lük dataframe olusturduk
df=pd.DataFrame(np.random.randn(3,3),index=("A","B","C"),columns=("colomn1","colomn2","colomn3"))
print(df)

#1. kolonuna ve 1-2 lolonlarına ulaştık
print(df["colomn1"])
print(df[["colomn1","colomn2"]])

#1.satıra ulasma
print(df.loc["A"])

#1-3 satırlara ulaşma
print(df.loc[["A","C"]])

#belirli bir elemana ulaşmak

print(df.loc["A","colomn2"])
print(df.loc[["A","B"],"colomn3"])

#bir aralıktaki değerler

print(df.loc[:,"colomn1":"colomn3"])

#yeni bir colomn eklemek 1 ve 2 colomn ların toplamı

df["colomn4"]=df["colomn1"]+df["colomn2"]
print(df)

df["colomn5"]=pd.Series(data=np.random.randn(3),index=["A","B","C"])
print(df)

#colomn silme
print(df.drop("colomn4",axis=1))