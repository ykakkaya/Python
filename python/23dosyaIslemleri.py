# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 
from asyncore import read


file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","w",encoding='utf-8')
file.write("yakup akkaya")
file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","a",encoding='utf-8')
file.write("\nyiğit akkaya\nelif akkaya")
file.write("\nhep beraber veri bilimine giriş dersindeyiz.")
file.close()
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","a",encoding='utf-8')
file.write("\nyakup akkaya"*5)
file.close()
print("************for ile okunanı yazdırma*********************")

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
try:
    file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile2.txt","x",encoding='utf-8')
except Exception as e:
    print(e)
    print("hata alındı")
finally:
    file.close()

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","r",encoding='utf-8')
for item in file:
    print(item)
file.close()
print("************read metodunu kullanma*********************")
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","r",encoding='utf-8')
okunan=file.read()
print(okunan)
file.close()
print("**************read metoduna karakter sayısını parametre verme*******************")
#sadece read metoduna girilen karakter kadar okuma yapar.
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","r",encoding='utf-8')
okunan=file.read(5)
print(okunan)
file.close()
print("************readline metodu kullanımı*********************")
#readline fonk. sadece bir satır okur.
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","r",encoding='utf-8')
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
file.close()
print("************readlines metodu kullanımı*********************")
#her satır bilgi liste elemanı gibi karşımıza çıkar liste şeklindede ulaşabiliriz 
file = open("C:\\Users\\Lenovo\\Desktop\\projeler\\newFile.txt","r",encoding='utf-8')
liste=file.readlines()
print(liste[4])
print(liste)

file.close()