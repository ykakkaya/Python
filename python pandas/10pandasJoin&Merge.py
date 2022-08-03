import pandas as pd
import numpy as np

customers = {
     'CustomerId': [1,2,3,4],
     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
     'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
 }

orders = {
     'OrderId': [10,11,12,13],
     'CustomerId': [1,2,5,7],
     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
      }

df1=pd.DataFrame(customers)
df2=pd.DataFrame(orders)
print(df1)
print(df2)

df3=pd.merge(df1,df2,how="inner") #kesişimleri alır
print(df3)
df4=pd.merge(df1,df2,how="left") #müşteriye karşılık order varsa alır yoksa nan döner
print(df4)
df5=pd.merge(df1,df2,how="right") # order karşılık müşteri varsa yazar yoksa nan döner
print(df5)
df6=pd.merge(df1,df2,"outer") # eşleşme olsun olmasın birleştirir eşleşmeyen değerlerin karşısında nan döner
print(df6)

print("*********************************************")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

af=pd.DataFrame(customersA)
af1=pd.DataFrame(customersB)
bf=pd.concat([af,af1],ignore_index =True)
print(bf)