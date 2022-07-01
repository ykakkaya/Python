website="http://www.ykakkaya.com"
course="python kursu: baştan sona python programlama kursu yaklaşık 40 saat"

#baştaki ve sondaki boşlukları silin
print("**************************************")
sent=' hello world '
sent= sent.strip()
print(sent)
print("**************************************")

# www.ykakkaya.com içinde ykakkaya dışındaki kısımları siliniz
print("**************************************")
url="www.ykakkaya.com"
url=url.lstrip("www.")
url=url.rstrip(".com")
print(url)
print("**************************************")

#course tüm karakterleri küçük yazın
print("**************************************")
course=course.lower()
print(course)
print("**************************************")

#website içinde kaç tane a var
print("**************************************")
print(website.count('a'))
print("**************************************")

#website www ile başlayıp com ile bitiyor mu
print("**************************************")
isStart= website.startswith('www')
print(isStart)
isFinish=website.endswith("com")
print(isFinish)
print("**************************************")

#website içinde .com varmı
print("**************************************")
isCom=website.find('.com')
print(isCom)
print("**************************************")

#course içindeki karakterlerin hepsi alfabetik mi
print("**************************************")
isAlphabet= course.isalpha()
print(isAlphabet)
isDigt=course.isdigit()
print(isDigt)
print("**************************************")

#Content ifadesini satırda 50 karakter içine ekle sağ ve soluna * koy
print("**************************************")
res="Content".center(50,"*")
print(res)

#50 karakter yer ayırır ama sola yaslar
res="content".ljust(50,"*")
print(res)

#50 karakter yer ayırır ama sağa yaslar
res="content".rjust(50,"*")
print(res)
print("**************************************")

#course içindeki tüm boşlukları - ile değiştir
print("**************************************")
course=course.replace(" ","-")
print(course)
print("**************************************")

#'hello world' içindeki world  python olarak değiştir
print("**************************************")
greeting="hello world"
greeting=greeting.replace("world","python")
print(greeting)
print("**************************************")

#course u boşluk karakterlerinden ayır
print("**************************************")
course=course.split("-")
print(course)
print("**************************************")
