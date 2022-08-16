# 1- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"1"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"1"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"0"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"0"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"1"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"1")


# 3- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

import pypyodbc
import pymssql

    
def insertDatas(list):

    conn=pypyodbc.connect(
        'Driver={SQL Server};'
        'Server=ykakkaya;'
        'Database=schooldb;'
        'UID=sa;'
        'PWD=kayseri38;')

    cursor=conn.cursor()

    sql="INSERT INTO std VALUES (?,?,?)"
    values=list
    result=cursor.executemany(sql,values)
    conn.commit()
    conn.close()


def selectDatas():
    conn=pypyodbc.connect(
        'Driver={SQL Server};'
        'Server=ykakkaya;'
        'Database=schooldb;'
        'UID=sa;'
        'PWD=kayseri38;')

    cursor=conn.cursor()
    sql="SELECT * FROM std"
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
        print(i)

sorgu=True
while sorgu:
    secim=int(input("veri girişi (1) sorgulama (2) cikış (3): "))
    
    if secim==1:
        list=[]
        while True:
            name=input("adınız : ")
            surname=input("soyadınız : ")
            gender=input("cinsiyet : ")
            list.append((name,surname,gender))
            bilgi=input("devam etmek istiyor musunuz?(e/h) :")
    
            if bilgi=="h":
                insertDatas(list)
                print("kayıt işlemi yapıldı")
                break
    elif secim==2:
        selectDatas()
        
    elif secim==3:
        print("çıkış işlemi yapıldı")
        sorgu=False
