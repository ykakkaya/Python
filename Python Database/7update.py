import pypyodbc
from connection import conn

def updating(id,name,surname,gender):
    cursor=conn.cursor()
    sql="UPDATE std SET stdName=?, stdSurname=? ,stdGender=? WHERE id=?"
    values=(name,surname,gender,id)
    cursor.execute(sql,values)
    cursor.commit()
    print(f"{id} ID NUMARALI kayıt güncellendi")
    conn.close()

name=input("name: ")
surname=input("surname: ")
gender= int(input("gender 0-1 : "))
id=int(input("güncellenecek id : "))
updating(id,name,surname,gender)