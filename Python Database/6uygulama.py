# 2- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci id, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   e- Kaç erkek öğrenci vardır ?
#   f- Kız öğrencileri harf sırasına göre getiriniz.

import pypyodbc
from connection import conn

def sorgu():
    cursor=conn.cursor()
    #sql="SELECT * FROM std"
    #sql="SELECT id,stdName,stdSurname FROM std"
    #sql="SELECT stdName,stdSurname FROM std WHERE stdGender=0"
    #sql="SELECT stdName,stdSurname FROM std WHERE (stdName LIKE '%an%') OR (stdSurname LIKE '%an%')"
    #sql="SELECT COUNT(*) FROM std WHERE stdGender=1"
    sql="SELECT COUNT(*) FROM std WHERE stdGender=0"
    cursor.execute(sql)
    res=cursor.fetchall()
    for i in res:
        print(i)
    conn.close()

sorgu()