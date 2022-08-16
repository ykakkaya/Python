import pymssql
import pypyodbc

def insertData(name,surname,gender):
    conn=pypyodbc.connect(
        'Driver={SQL Server};'
        'Server=ykakkaya;'
        'Database=schooldb;'
        'UID=sa;'
        'PWD=kayseri38;')
    cursor= conn.cursor()
    sql="INSERT INTO std  VALUES (?,?,?)"
    values=(name,surname,gender)
    result=cursor.execute(sql,values)
    conn.commit()
    print(f"{cursor.rowcount} adet kayıt eklendi")
    
    conn.close()


def insertDatas(list):
    conn=pypyodbc.connect(
        'Driver={SQL Server};'
        'Server=ykakkaya;'
        'Database=schooldb;'
        'UID=sa;'
        'PWD=kayseri38;')
    cursor= conn.cursor()
    sql="INSERT INTO std  VALUES (?,?,?)"
    values=list
    result=cursor.executemany(sql,values)
    conn.commit()
    print("kayıt eklendi")
    
    conn.close()

list=[]
while True:    
    name=input("ad: ")
    surname= input("soyad: ")
    gender= int(input("cinsiyet(kız=0 erkek=1) :"))
    list.append((name,surname,gender))
    con=input("devam etmek istiyor musunuz?(e/h) :")
    
    if con=="h":
        insertDatas(list)
        print("kayıt işlemi yapıldı")
        break   
    