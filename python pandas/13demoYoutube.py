from statistics import mean
import pandas as pd
import numpy as np

df=pd.read_csv("datasets/youtube-ing.csv")

print(df.info())
# 1- İlk 10 kaydı getiriniz.
print("1- İlk 10 kaydı getiriniz.")
print(df.head(10))
print("***********************************")

# 2- İkinci 5 kaydı getiriniz.
print("2- İkinci 5 kaydı getiriniz.")
print(df[5:10])
print("***********************************")

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
print("Dataset' de bulunan kolon isimleri ve sayısını bulunuz.")
print(len(df.columns))
print(df.columns)
print(df.columns.value_counts())
print("***********************************")
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
print("thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description kolonlarını siliniz")
af=df.copy()
af=df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)
print(af.columns)
print("***********************************")

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.

print("Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.")
print(f"beğenme sayıları ortalaması = {af['likes'].mean()}")
print(f"beğenmeme sayıları ortalaması = {af['dislikes'].mean()}")
print("***********************************")

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
print("ilk 50 videonun like ve dislike kolonlarını getiriniz")
print(af.head(50)[["title","likes","dislikes"]])
print("***********************************")

# 7- En çok görüntülenen video hangisidir ?
print("7- En çok görüntülenen video hangisidir ?")
print(af[af["views"].max()==af["views"]]["title"].iloc[0])
print("***********************************")
# 8- En düşük görüntülenen video hangisidir?
print("8- En düşük görüntülenen video hangisidir?")
print(af[af["views"].min()==af["views"]]["title"].iloc[0])
print("***********************************")
# 9- En fazla görüntülenen ilk 10 video hangisidir ?
print(" 9- En fazla görüntülenen ilk 10 video hangisidir ?")
print(af.sort_values("views",ascending=False)[["title","views"]].iloc[:10])
# ikinci yol ==> print(df.sort_values("views", ascending=False).head(10)[["title","views"]])
print("***********************************")


# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
print("10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.")
print(af.groupby("category_id").aggregate("mean").sort_values("likes")["likes"])
print("***********************************")
# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
print("11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.")
print(af.groupby("category_id").aggregate("sum").sort_values("comment_count",ascending=False)["comment_count"])
print("***********************************")
# 12- Her kategoride kaç video vardır ?
print("12- Her kategoride kaç video vardır ?")
print(af["category_id"].value_counts())
print("***********************************")
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
print("13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.")
af["titleLenght"]=af["title"].apply(len)
print(af.head(5))
print("***********************************")
# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
print("14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.")
print(af["tags"].head(3))

af["tags_count"]=af["tags"].apply(lambda x : len(x.split("|")))
print(af.head(3))
print("***********************************")
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
print("15- En popüler videoları listeleyiniz.(like/dislike oranına göre)")
def ortHes(data):
    popularData=[]
    like=list(data["likes"])
    dislike=list(data["dislikes"])
    allData=list(zip(like,dislike))
    
    for like,dislike in allData:
        if (like+dislike)==0:
            popularData.append(0)
        else:
            popularData.append(like/(like+dislike))

    return popularData

af["popular"]=ortHes(df)
print(af.sort_values("popular",ascending=False)[["title","likes","dislikes","popular"]])

print("***********************************")
