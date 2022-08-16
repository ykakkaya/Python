import pypyodbc
from connection import conn

def getStd(gender):
    cursor=conn.cursor()
    sql="SELECT * FROM std WHERE stdGender=?"
    params=(gender,)
    cursor.execute(sql,params)
    res=cursor.fetchall()
    for i in res:
        print(i)

gender=int(input("0-1 : "))
getStd(gender)