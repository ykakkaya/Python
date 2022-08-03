import pandas as pd
import numpy as np

data={
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

def kareAl(x):
    return x**2

kareAl2= lambda x: x**2  #lambda metod tanımlama

df=pd.DataFrame(data)
print(df)

print(df["Column2"].unique())  # uniq elemanları getirir
print(df["Column2"].nunique()) #uniq eleman sayısını getirir
print(df["Column2"].value_counts()) #her elemandan kaç tane olduğunu döner
print(kareAl(df["Column1"]))
print(df["Column2"].apply(kareAl2)) # apply metoduna parametre olarak  kullanılacak metodu gönderebiliriz
print(df["Column1"].apply(lambda x: x**2))
df["Column4"]=df["Column3"].apply(len)
print(df)

data1 = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df1 = pd.DataFrame(data1)
print(df1)
print("****************************************************")
df2=df1.groupby(["Ay","Kategori"]).aggregate(np.sum).T
print(df2)
print("*****************************************")
df3=df1.pivot_table(index="Ay",columns="Kategori",values="Gelir")
print(df3)