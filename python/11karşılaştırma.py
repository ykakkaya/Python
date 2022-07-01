#girilen iki sayıdan büyük olan

num1=float(input("1.sayı: "))
num2=float(input("2. sayı : "))

if(num1> num2):
    print("1.sayı büyük")
else:
    print("2.sayı büyük")

#kullanıcıdan 2 vize(%60) 1 final notu(%40) al ort. 50 üstü geçer

vize1=float(input("1. vize: "))
vize2= float(input("2.vize: "))
final= float(input("final notu: "))
result= ((vize1+vize2)*0.6)+(final*0.4)
if(result>=50):
    print("dersi geçtiniz")
else:
    print("dersten kaldınız")


#girilen bir sayının tekmi çift mi olduğunu yazdır

a=int(input("1.sayı: "))

if(a%2==0):
    print("çift sayı")
else:
    print("tek sayı")

#girilen bir sayının pozitif negatif olmasını yazdır

b=int(input("1.sayı: "))
if(b>0):
    print("pozitif sayı")
else:
    print("negatif sayı")

#parola e mail bilgisi iste kontrol et
password="12345" 
email= "ykakkaya@hotmail.com"

mail=input("mail adresini giriniz: ")
passw=input("parola giriniz: ")

if(mail==email)&(password==passw):
    print("giriş başarılı hoşgeldiniz")
else:
    print("giriş bilgileriniz hatalı")

