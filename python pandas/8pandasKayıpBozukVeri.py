import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])
print(df)
print("***********************************")
#yeni bir column eklemek
newColumn=[np.nan,45,np.nan,14,np.nan,78,np.nan,13]
df['column4']=newColumn

#column veya satır silme işlemi

print(df.drop(["column1","column3"],axis=1))
print(df.drop(["a","d","h"],axis=0))

print("**********************************************")
#boş veri olan ve dolu olan satır sutunların bulunması

print(df.isnull())
print(df.notnull())

print(df)
print(df.isnull().sum())
print(df["column1"].isnull().sum())

print(df[df['column1'].isnull()]["column1"])
print(df[df['column1'].notnull()]["column1"])

# BİR SATIRDA NaN değer varsa dropna() metoduyla o satır veya sutunu silebiliriz
#axis değeri varsayılanı axis=0 dır.

print(df.dropna()) #satırda silme yapar
print(df.dropna(axis=1)) ##sütunda silme yapar

print(df.dropna(how="any")) #enza 1 nan varsa siler
print(df.dropna(how="all")) #hepsi nan ise siler
print(df.dropna(subset=["column1","column2"])) #istediğimiz kolonlarda nan varmı diye bakar

print(df.dropna(thresh=3)) #enaz belirtilen kadar tam veri olursa silmez yoksa siler

#boş alanlara veri girişi yapabiliriz fillna() metoduyla

print(df.fillna(value="no input"))
print(df.fillna(value=df.mean())) #her sutunun ortalamasını nan alanlarına ekledi

ort=df.mean().mean() # tüm dataframe in ortalaması
print(f"dataframe ortalaması = {ort}")
print(df)
print(df.fillna(value=ort))


