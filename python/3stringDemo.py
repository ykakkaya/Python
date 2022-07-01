from audioop import reverse


website="http://www.ykakkaya.com"
course="pythonkusu: baştan sona python programlama kursu yaklaşık 40 saat"

print("course karakter dizisinde kaç karakter bulunuyor?")
print(len(course))

print("website içindeki www karakterlerini alalım")
print(website[7:10])

print("website içindeki com karakterini alalım")
print(website[len(website)-3:])

print("course içindeki ilk 15 ve son 15 karakteri alalım")
print(course[0:15])
print(course[len(course)-15:])

print("course karakter dizisini tersten yazalım")
print(course[::-1])

name,surname,age,job= "bora","yılmaz",32,"mühendis"

print(f"benim adım {name} {surname} yaşım {age} ve mesleğim {job}")

#Hello world ifadesindeki w W olarak değistir.
s="hello world"
s=s[0:6]+'W'+s[-4:]

#replace metodu ile de bu şekilde yapılır.
#s=s.replace('w','W')
print(s)

#abc ifadesini yanyana 3 defa yazdırın
print("abc"*3)
