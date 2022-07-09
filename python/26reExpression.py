import re

str="Python Kursu: Python programlama rehberiniz yaklaşık 40 saat içerik."
#verilen ifadeden kaç tane olduğunu buluruz.

print(len(re.findall("Python",str)))

#verilen ifaeyi kriterimize göre split eder
s1=re.split(" ",str)
print(s1)

#verilen bir ifadeyi değiştirme boşlukları - ile değiştirdik
s2=re.sub(" ","-",str)
print(s2)

#verilen bir ifadeyi arama ilk bulduğu yeri döner
s3=re.search("40",str)
print(s3)
#ilk bulduğu değerin bitiş ve başlama indeksi
print(s3.end())
print(s3.start())
#arama yapılan string ifadeyi döner
print(s3.string)

"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   

         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""
#str içerisinse s a t karakterlerini arar
r1=re.findall("[sat]",str)
print(r1)
#a-z dışındaki bütün karakterler döner
r2=re.findall("[^a-z]",str)
print(r2)

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

    
"""
#Py den sonra herhangi iki karakter somra on ile biten kelimeleri getirir.
r3=re.findall("Py..on",str)
print(r3)

"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""
r4=re.findall("^P",str)
print(r4)
"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

r5=re.findall("sa*t",str)
print(r5)
"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""


"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""
r6=re.findall("(p|P)yt",str)
print(r6)


"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı

        result = re.findall("\APython", str)
        
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
        result = re.findall("saat\Z", str)

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""

