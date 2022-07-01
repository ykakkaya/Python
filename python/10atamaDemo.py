x,y,z=2,5,10
numbers=1,5,7,10,6

#kullanıcıdan iki sayı al ve çarpımını bul.sonucun x,y,z toplamından farkı nedir

num1=float(input("birinci sayıyı giriniz"))
num2=float(input("ikinci sayıyı giriniz"))
result=(num1*num2)-(x+y+z)
print(result)
print("***********************")

#y nin x e kalansız bölümünü hesaplayınız

print(y//x)
print("***********************")

#(x,y,z)toplamının mod 3 ü nedir

print((x+y+z)%3)
print("***********************")

#y nin x .inci kuvvetini hespla

print(y**x)
print("***********************")

#x,*y,z =numbers işlemine göre z nin küpü

x,*y,z =numbers
print(z**3)
x,*y,z =numbers
print("***********************")

#x,*y,z=numbers isleminde y nin değerler toplamı nedir

sum=y[0]+y[1]+y[2]
print(sum)
