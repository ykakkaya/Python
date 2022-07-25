import numpy as np

numbers1=np.random.randint(1,100,8)
numbers2=np.random.randint(1,100,8)
print(numbers1)
print(numbers2)

#verilen dizileri toplama aynı indeksdeki elemanlar toplanır.
print(f"verilen dizilerin toplamı=\n {numbers1+numbers2}")
#her indeks elemanına eklenir.
print(f"verilen diziye (numbers1) istediğimiz elemanı(10) eklersek=\n {numbers1+10}")
#aynı indeksdeki elemanlar çıkarılır.
print(f"verilen dizilerin farkı=\n {numbers1-numbers2}")
#her indeksten verilen değer çıkarılır.
print(f"verilen dizilerin(numbers2) istediğimiz elemenı(40) çıkarma=\n {numbers2-40}")
#aynı indeksdeki elemanlar çarpılır-bölünür.
print(f"verilen dizilerin çarpımı=\n {numbers1*numbers2}")
print(f"verilen dizilerin bölümü=\n {numbers1/numbers2}")
print(f"verilen dizi(numbers1) elemanlarını (5) ile  çarpma=\n {numbers1*5}")
print(f"verilen dizi(numbers2) elemanlarını (10) ile  bölme=\n {numbers2/10}")

mNum=numbers1.reshape((2,4))
print(mNum)
mNum2=numbers2.reshape((2,4))
print(mNum2)

mVerticalAdd=np.vstack((mNum,mNum2))
print(mVerticalAdd)

mHorizantelAdd=np.hstack((mNum,mNum2))
print(mHorizantelAdd)

#matrislerin verilen şarta uygunluğunu kontrol etmek için true false döner
print(numbers1)
print(numbers1<=45)
print(numbers1%2==0)
#istediğimiz şartı sağlayan elemanları bulmak için
evenArray=numbers2%2==0
print(numbers2)
print(numbers2[evenArray])