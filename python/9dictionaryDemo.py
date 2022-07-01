# öğrenci numarası adı soyadı telefonun olduğu ve bilgilerin kullanıcıdan alındığı dictionary yaz
students={}
stdNumber= input("öğrenci numarasını giriniz")
stdName=input("öğrenci adını giriniz")
stdSurname=input("öğrencinin soyadını giriniz")
stdTelephone=input("öğrencinin telefonunu giriniz")

students.update({
    stdNumber:{
        'ad':stdName,
        'soyad':stdSurname,
        'telephone':stdTelephone
    }
})

stdNumber= input("öğrenci numarasını giriniz")
stdName=input("öğrenci adını giriniz")
stdSurname=input("öğrencinin soyadını giriniz")
stdTelephone=input("öğrencinin telefonunu giriniz")

students.update({
    stdNumber:{
        'ad':stdName,
        'soyad':stdSurname,
        'telephone':stdTelephone
    }
})

stdNumber= input("öğrenci numarasını giriniz")
stdName=input("öğrenci adını giriniz")
stdSurname=input("öğrencinin soyadını giriniz")
stdTelephone=input("öğrencinin telefonunu giriniz")

students.update({
    stdNumber:{
        'ad':stdName,
        'soyad':stdSurname,
        'telephone':stdTelephone
    }
})
print(students)

stdNumber=input("öğrenci no giriniz")

print(students[stdNumber])