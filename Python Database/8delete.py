import pypyodbc
from connection import conn

def deleteStd(id):
    cursor=conn.cursor()
    sql="delete from std where id=?"
    params=(id,)
    cursor.execute(sql,params)
    cursor.commit()
    print(f"{id} nımaralı kayıt silindi")
    conn.close()

id=int(input("id: "))
deleteStd(id)