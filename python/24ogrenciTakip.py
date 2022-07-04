def notHesapla():
    with open("C:\\Users\\Lenovo\\Desktop\\projeler\\ögrenciler.txt","r",encoding="utf-8") as file:
        
        liste=file.readlines()
        for item in liste:
            #print(item)
            item = item[:-1]
            list = item.split(':')

            ogrenciAdi = list[0]
            notlar = list[1].split(',')

            not1 = int(notlar[0])
            not2 = int(notlar[1])
            not3 = int(notlar[2])

            ortalama = (not1+not2+not3)/3
            print(f"{ogrenciAdi} ortalaması: {ortalama}")   
       
            


def stdKayit():
    stdName=input("öğrenci adını giriniz: ")
    stdSurname=input("öğrenci soyadını giriniz: ")
    stdLesson=input("dersı giriniz: ")
    not1=int(input("not1 giriniz: "))
    not2=int(input("not2 giriniz: "))
    not3=int(input("not3 giriniz: "))
    with open("C:\\Users\\Lenovo\\Desktop\\projeler\\ögrenciler.txt","a",encoding="utf-8") as file:
        file.write(f"{stdName} {stdSurname} öğrencisinin {stdLesson} dersi notları:{not1},{not2},{not3}\n")



def stdListe():
    with open("C:\\Users\\Lenovo\\Desktop\\projeler\\ögrenciler.txt","r",encoding="utf-8") as file:
            print(file.read())




start=True
while(start):
    sec1=int(input("1-öğrenci not kayıt\n2-öğrenci listesi\n3-ortalama bilgisi\n4-çıkış\nİŞLEM NUMARASI GİRİNİZ: "))
    if(sec1==1):
        stdKayit()   
    elif(sec1==2):
        stdListe()
    
    elif(sec1==3):
        notHesapla()
   
    elif(sec1==4):
        start=False
        print("çıkış işlemi yapıldı")