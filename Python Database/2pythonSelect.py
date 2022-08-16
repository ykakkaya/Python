import pypyodbc

def selectData():
    conn=pypyodbc.connect(
        'Driver={SQL Server};'
        'Server=ykakkaya;'
        'Database=schooldb;'
        'UID=sa;'
        'PWD=kayseri38;')
    cursor=conn.cursor()
    sql="SELECT * FROM std"
    cursor.execute(sql)
    result= cursor.fetchall()
    for item in result:
        print(item)
    

selectData()