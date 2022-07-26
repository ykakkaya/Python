from multiprocessing import connection
import pandas as pd
import sqlite3

#csv dosyasını okuma
df=pd.read_csv("datasets//sample.csv")
print(df)

#json dosyasını okuma
df1=pd.read_json("datasets//sample.json")
print(df1)

#excel dosyasını okuma

df2=pd.read_excel("datasets//sample.xlsx")
print(df2)

#database dosyası okuma
connection=sqlite3.connect("datasets//sample.db")
df3=pd.read_sql_query("SELECT * FROM students",connection)
print(df3)