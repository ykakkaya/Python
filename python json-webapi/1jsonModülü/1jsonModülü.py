#json işlemlerini yapmak için bu modülü import etmemiz gerekiyor
import json

#dictionary yapımız aşağıdaki gibidir.
person={"name":"ali","languages":["python","java"]}
print(person["name"])
print(person["languages"])
print(person["languages"][0])

#json yapısını dict. yapısına  çevirmek için 
print("**********json yapısını dict yapısına dönüştürme*********")
#gelen json bilgisi 
person_str='{"name":"ali","languages":["python","java"]}'
#json u dict çevirdik ve elemanlarına artık ulaşıyoruz.
result=json.loads(person_str)
print(result)
print(type(result))
print(result["name"])
print(result["languages"][1])


#dosyadan json bilgileri okuma
print("******dosyadan json bilgiyi okuma********")
with open("person.json") as f:
    data=json.load(f)
    print(data)
    print(data["name"])

#dict bilgiyi json a çevirme
print("******dict to json********")
person_dict={"name":"yakup","languages":["python","java","C#"]}

jresult=json.dumps(person_dict,indent=4,sort_keys=True)
print(jresult)
print(type(jresult))

#dosyaya eklemek için
print("******dosyaya json bilgiyi yazma********")
with open("person.json","a") as file:
    json.dump(person_dict,file)

