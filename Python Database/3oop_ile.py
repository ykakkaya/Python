
import pypyodbc
from connection import conn

class Student():
    connection=conn
    mycursor=connection.cursor()

    def __init__(self,stdName,stdSurname,stdGender):

        self.stdName=stdName
        self.stdSurname=stdSurname
        self.stdGender=stdGender

    def saveStudent(self):
        sql="INSERT INTO std VALUES (?,?,?)"
        values=(self.stdName,self.stdSurname,self.stdGender)
        self.mycursor.execute(sql,values)
        self.connection.commit()
        print("kayıt eklendi")
        self.connection.close()

    @staticmethod
    def saveStudents(list):
        sql="INSERT INTO std VALUES (?,?,?)"
        values=(list)
        Student.mycursor.executemany(sql,values)
        Student.connection.commit()
        print("kayıtlar eklendi")
        Student.connection.close()

# tek kayıt ekleme
std=Student("Ahmet","Demir",1)
std.saveStudent()


#liste olarak ekleme
list=[("uğur","usta",1),("murat","köseoğlu",1),("çiğdem","şahin",0),("rana","akdaş",0),("furkan","demir",1)]
Student.saveStudents(list)

