#string ifadelerin birleştirilmesi

name='yakup'
surname='kaya'
age=38
greeting='my name is '+name+'\nsurname '+surname+'\nmy age '+str(age)

print("cümlemizin tamamı: ")
print(greeting)

print("cümlemizin uzunluğu: ")
print(len(greeting))

print("cümlenin ilk karakteri: ")
print(greeting[0])

print("cümlenin 5. karakteri: ")
print(greeting[5])

print("cümlenin son karakteri: ")
print(greeting[-1])

print("cümlenin 4. karakteri ile 14. karakteri arası: ")
print(greeting[3:14])

print("baştan 10. karaktere kadar:")
print(greeting[:10])

print("3. karakterden 38. karaktere kadar 1 er atlayarak")
print(greeting[2:38:2])

#string lerle format oluşturma
#stringleri parametreleri girerek birleştirme .format ile
print('my name is {0} and surname is {1}'.format(name,surname))
print("my name is {1} and surname is {0} ".format(name,surname))
print("my name is {0} and surname is {1} and I'm {2} years old".format(name,surname,age))

#f string formatlama yöntemi

print(f"my name is {name} {surname} and my age {age}")
