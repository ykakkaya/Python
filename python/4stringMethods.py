message= "merhaba herkese. python programlama öğreniyorum."

#upper metodu tüm karakterleri büyük yapar.
message=message.upper()

#lower tüm karakterleri küçük yapar.
message=message.lower()

#title metodu her kelimenin baş harfini büyük yapar.
message=message.title()

#capitilize metodu verilen string ifadenin sadece ilk harfini büyük yazar
message=message.capitalize()

#strip metodu string ifadenin en başında ve sonunda  boşluk varsa siler
message=message.strip()

#split metodu da verilen değere göre string ifadeyi parçalar.
message=message.split() #bu şekilde boşluklardan ayırır.
print(message[-1])
print (message[0])
#message=message.split('.') bu şekilde noktalardan ayırır.

#join den önceki boşluk her eklenen kelimenin arasına boşluk bırakır.
message=' '.join(message)

#find metodu aradığımız bir kelimenin ilk harfinin index ini döner
index=message.find("python")
print(index)

#replace ilk aldığı parametre yerine ikinci aldığı parametreyi yazar
message=message.replace('python','PYTHON')
print(message)