#ilk python kodu
import math


print('merhaba python')

#python input alma ve tip dönüşümü
num1= input('1.sayıyı giriniz')
num2=input('2. sayıyı giriniz')
total=float(num1) + float(num2)
print(total)

#dairenin çevre alanını hesaplama
r=float(input('dairenin yarıçapını giriniz'))
alan=math.pi*r
print('alan: ',alan)
cevre=2*math.pi*r
print('cevre: ',cevre)