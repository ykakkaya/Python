import pandas as pd
import numpy as np

df=pd.read_csv("datasets//nba.csv")



# 1- İlk 10 kaydı getiriniz.

print(df.head(10))
print("************************************************")

# 2- Toplam kaç kayıt vardır ?

print(len(df.index))
print("************************************************")
# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?


ort=df["Salary"].mean()
print(ort)
print("************************************************")
# 4- En yüksek maaşı ne kadardır ?

dmax=df["Salary"].max()
print(dmax)
print("************************************************")
# 5- En yüksek maaşı alan oyuncu kimdir ?


result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
print(result)

print("************************************************")
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
filt=(df["Age"]>=20) & (df["Age"]<=25)
print(df[filt][["Name","Team","Age"]].sort_values("Age",ascending=False))
print("************************************************")
# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
print(df[df["Name"] == "John Holland"]["Team"].iloc[0])
print("************************************************")
# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?

af=df.groupby("Team")["Salary"].aggregate(np.mean)
print(af)
print("************************************************")
# 9- Kaç farklı takım mevcut ?

print(df["Team"].nunique())
print("************************************************")
# 10- Her takımda kaç oyuncu oynamaktadır ?

tf=df.groupby("Team")["Name"].aggregate("count").T
print(tf)

print(df["Team"].value_counts())

print("************************************************")
# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace = True)
print(df[df["Name"].str.contains("and")])