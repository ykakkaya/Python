# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

from operator import truediv


def yaz(word,count):
    print(word*count)

yaz("elif",5)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
def changeList(*params):
    list=[]
    for p in params:
        list.append(p)
    print(list)

changeList(1,4,7,8,5,2,6,8,4,6,65,65,25,21)



# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalSayılariBul(sayi1, sayi2):
     for sayi in range(sayi1, sayi2+1):
         if sayi > 1:
             for i in range(2, sayi):
                 if (sayi % i == 0):
                     break
             else:
                 print(sayi)

 
asalSayılariBul(10, 20)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def bolenBul(num):
    list=[]
    i=1
    while(i<=num):
        if(num%i==0):
            list.append(i)
        i+=1
    print(list)

bolenBul(20)