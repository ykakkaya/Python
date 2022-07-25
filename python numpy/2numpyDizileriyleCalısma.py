import numpy as np

#kendimiz array a eleman atayabiliriz
array1= np.array([1,3,5,7,9])
print(array1)

#belirli aralıkta istediğimiz sartta eleman atayabiliriz
array2=np.arange(2,10,2)
print(array2)

#sadece 0 veya 1 lerle oluşturabiliriz
array3=np.zeros(10)
print(array3)
array4=np.ones(5)
print(array4)

#belirttiğimiz aralığı belirttiğimiz parçaya böler
array5=np.linspace(0,100,5)
print(array5)

#random ile rastgele sayı üretebiliriz
#baslama bitiş değeri veya sadece bitiş değerini de verebiliriz
#rastgele sayıyı istediğimiz adette dizi olarak dönebiliriz.

i=1
while(i<6):
    ran=np.random.randint(1,10)
    print(ran)
    i+=1
#1 ile 35 arasında 8 tane rastgele sayı üretip max olanı bul
ran2=np.random.randint(1,35,8)
print(ran2)
print(f"üretilen sayılardan en büyüğü= {ran2.max()}")
print(f"üretilen sayılardan en küçüğü= {ran2.min()}")
print(f"üretilen sayıların ortalaması= {ran2.mean()}")
print(f"üretilen sayıların en büyük olanın indeksi= {ran2.argmax()}")
print(f"üretilen sayıların en küçük olanın indeksi= {ran2.argmin()}")


np_array=np.arange(50)
np_matris=np_array.reshape(5,10)
print(np_matris)

#matristeki satırların toplamı
sumSatır=np_matris.sum(axis=1)
print(f"satırların toplamı= {sumSatır}")
sumSutun=np_matris.sum(axis=0)
print(f"sutunların toplamı = {sumSutun}")
