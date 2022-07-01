#girilen bir sayının 0-100 aralığında olup olmadığı

x=int(input("bir sayı giriniz"))

if(x>0 & x<100):
    print("sayımız 0-100 aralığındadır.")
else:
    print("sayımız 0-100 aralığında değildir.")
print("**********************************")
#girilen bir sayının pozitif çift sayı olup olmadığı

y=int(input("bir sayı giriniz"))
if((y>0) & (y%2==0)):
    print("sayımız pozitif çift sayıdır")
else:
    print("sayımız pozitif çift değildir.")
print("**********************************")

#email ve parola bilgileri ile giriş kontrolü yapma
email="ykakkaya@hotmail.com"
password="12345"

mail=input("mail adresini giriniz")
passw=input("şifrenizi giriniz")
if((mail==email) & (password==passw)):
    print("giriş başarılı")
else:
    print("hatalı giriş yapıldı")

print("**********************************")
#2 vize (%60) 1 final(%40) geçme notu 50 olmalı
    #final enza 50 olmalı
    #final 70 ve üstü ise vize önemli değil
vize1=int(input("birinci vize sınavını giriniz"))
vize2=int(input("ikinci vize sınavını giriniz"))
finalNot=int(input("final notunu giriniz"))
ort=float((((vize1+vize2)/2)*0.6)+(finalNot*0.4))
if((ort>50 & finalNot>=50) or (finalNot>=70)):
    print("dersi geçtiniz")
else:
    print("dersten kaldınız")

#kilo/boyun karesi(vki)
    #0-18,4 zayıf
    #18,5-24,9 normal
    #25-29,9 fazla kilolu
    #30-34,9 obez

kilo=float(input("kilo bilginiz: "))
boy=float(input("boy bilginiz: "))
vki= kilo/boy**2
if((vki>0) & (vki<=18.4)):
    print("zayıfsınız")
elif((vki>=18.4) & (vki<=24.9)):
    print("kilonuz normal")
elif((vki>24.9) & (vki<=29.9)):
    print("fazla kilolusunuz")
elif((vki>=30) & (vki<=34.9)):
    print("obezsiniz")
