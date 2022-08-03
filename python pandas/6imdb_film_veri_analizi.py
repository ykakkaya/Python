import pandas as pd

df=pd.read_csv("datasets//imdb.csv")


print("1- Dosyada hakkındaki bilgiler.") 
print(df.columns)
print(df.info())
print("***********************************")

print("2- ilk 5 kaydı gösterin")
print(df.head())
print("***********************************")


print("3- ilk 10 kaydı gösterin")
print(df.head(10))
print("***********************************")

print("4- Son 5 kaydı gösterin")
print(df.tail(5))
print("***********************************")
 
print("5- Son 10 kaydı gösterin")
print(df.tail(10))
print("***********************************")

print("6- Sadece Movie_Title kolonunu alın.")
print(df["Movie_Title"])
print("***********************************")


print("7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.")
print(df["Movie_Title"].head(5))
print("***********************************")
 
print("8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.")
print(df[["Movie_Title","Rating"]].head(5))
print("***********************************")


print(" 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.")
print(df[["Movie_Title","Rating"]].tail(7))
print("***********************************")
 

print("10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın.")
print(df[5:][["Movie_Title","Rating"]].head())
print("***********************************")


print("11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız.")
filt=df["Rating"]>=8
print(df[filt][["Movie_Title","Rating"]].head(50))

print("***********************************")
 

print("12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.")

filt2= (df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)
print(df[filt2])
print("***********************************")

 

print('13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listeleyiniz.')

filt3=(df["Num_Reviews"]>=100000) | (df["Rating"]>=8) & (df["Rating"]<=9)

print(df[filt3][["Movie_Title","Num_Reviews","Rating"]])