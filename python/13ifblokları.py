#isim yaş eğitim bilgisi al ehliyet alıp alamayacağını sorgula
#18 yaşından büyük lise veya üni. mezunu

from ast import alias


ad=input("adınızı giriniz: ")
yas=int(input("yasınızı giriniz: "))
egitim=input(" ilkokul mezunu 1 \n ortaokul mezunu 2 \n lise 3 \n üniversite 4 \n")
if((yas>=18)& (egitim=="3" or egitim=="4")):
    print(f"{ad} ehliyet alabilirsin")
else:
    print(f"{ad} ehliyet alma şartları taşımıyorsun")
print("************************************")

#trafiğe çıkan bir aracın servis bakım zamanını hesaplayınız
    #1.bakım tarihi
    #2.bakım tarihi
    #3. bakım tarihi
#bakım zamanını alınan gün ay yıla göre hesaplab(datetime modülü kullanılacak)

import datetime

trafigeCıkıs=input("aracın trafiğe cıkış zamanını giriniz yıl/ay/gün şeklinde")
tarih=trafigeCıkıs.split("/")
dateTrafik= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()

fark=simdi-dateTrafik
print(fark.days)
if(fark.days<365):
    print("1. servis aralığı")
elif((fark.days>365) & (fark.days<365*2)):
    print("2. bakım aralığı")
elif((fark.days>365*2) & (fark.days<365*3)):
    print("3. bakım aralığı")
else:
    print("farklı bakım aralığı")