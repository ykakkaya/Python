import numpy as np


# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
np_array=np.array([10,15,30,45,60])
print(np_array)

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

np_array2=np.arange(5,15)
print(np_array2)

#3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

np_array3=np.arange(50,100,5)
print(np_array3)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

np_array4=np.zeros(10)
print(np_array4)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

np_array5=np.ones(10)
print(np_array5)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

np_array6=np.linspace(0,100,5)
print(np_array6)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.

np_array7=np.random.randint(10,30,5)
print(np_array7)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.

np_array8=np.random.randn(10)
print(np_array8)

# 9- (3x5) boyutlarında (-50-50) arasında rastgele bir matris oluşturunuz.

np_arr=np.random.randint(-50,50,15)
m_arr=np_arr.reshape(3,5)
print(m_arr)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız 

sumRow= m_arr.sum(axis=1)  #satırlar
sumCol=m_arr.sum(axis=0)  #sütunlar
print(sumRow)
print(sumCol)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir 

maxItem=m_arr.max()
minItem=m_arr.min()
averageItems=m_arr.mean()
print(m_arr)
print(maxItem)
print(minItem)
print(averageItems)


# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?
maxIndex=m_arr.argmax()
minIndex=m_arr.argmin()
print(maxIndex)
print(minIndex)

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

np_arr1=np.arange(10,20)
print(np_arr1[0:3])

# 14- Üretilen dizinin elemanlarını tersten yazdırın.

print(np_arr1[::-1])

# 15- Üretilen matrisin ilk satırını seçiniz.

print(m_arr[0])

# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?
print(m_arr)
print(m_arr[1][2])

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

print(m_arr[:,0])

# 18- Üretilen matrisin her bir elemanının karesini alınız.

print(m_arr**2)

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ?

m_arrEven= (m_arr%2==0)&(m_arr>0)
print(m_arr)
print(m_arr[m_arrEven])