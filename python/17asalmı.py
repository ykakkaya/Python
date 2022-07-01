'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''

from operator import truediv


number=int(input("bir sayı giriniz: "))
isAsal=False
if number==1:
    isAsal=False
elif number==2:
    isAsal=True
else:
    i=2
    while(i<int(number)):
        if(number%i==0):
            isAsal=False
            break
        else:
            isAsal=True
        i+=1
if(isAsal):
    print(f"{number} sayısı asaldır")
else:
    print(f"{number} sayısı asal değildir")
