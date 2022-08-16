import pypyodbc
from connection import conn

def stdAgg():
    cursor=conn.cursor()
    #sql="SELECT COUNT(*) FROM std"
    #sql="SELECT COUNT(*) FROM std WHERE stdGender=0"
    #sql="SELECT * FROM std WHERE stdGender=0 ORDER BY stdName"
    #sql="SELECT COUNT(*) FROM std WHERE stdName='yiğit'"
    #sql="SELECT * FROM std WHERE stdName LIKE 'A%'"
    sql="SELECT COUNT(*) FROM std WHERE stdName LIKE 'A%'"
    cursor.execute(sql)
    res=cursor.fetchall()
    print(res)


stdAgg()