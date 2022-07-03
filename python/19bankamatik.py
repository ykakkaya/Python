#kullanıcı ekle (sınırsız)
# kullanıcıları listele 
#müsteri no ile müşteri bulma
#bakiye görüntüle
#para çek ve para yatır. 


from asyncio.windows_events import NULL


customers=[]

def customerAdd():
    mNo=int(input("müşteri numarasını giriniz: "))
    name=input("müsteri adını giriniz: ")
    surnamme=input("müşteri soyadını giriniz: ")
    bakiye=int(input("ilk hesap açılış bakiyesi: "))
    customers.append(
        {

            'mNo':mNo,
            'name':name,
            'surname':surnamme,
            'bakiye':bakiye
        
            
    })
def  moneyAdd(mNo):
    
    for c in customers:
        if(c['mNo']==mNo):
            
            price=int(input("yatırılacak miktarı giriniz: "))
            c['bakiye']+=price
            print(f"{price} para hesaba eklendi yeni bakiye {c['bakiye']}")
            break

def  moneyPull(mNo):
    
    for c in customers:
        if(c['mNo']==mNo):
            
            price=int(input("çekilecek para miktarı giriniz: "))
            if(c['bakiye']>= price):
                c['bakiye']-=price
                print(f"{price} para hesaba eklendi yeni bakiye {c['bakiye']}")
                break
            else:
                print(f"bakiyeniz yetersiz en fazla {c['bakiye']} çekebilirsiniz")

def customerList():
    for c in customers:
        print(f"{c['mNo']} hesabının sahibi {c['name']} {c['surname']} kişinin bakiyesi {c['bakiye']}\n")

def customerFind(mNo):
    for c in customers:
        if(c['mNo']==mNo):
            print(f"{c['mNo']} hesabının sahibi {c['name']} {c['surname']} kişinin bakiyesi {c['bakiye']}")
            





customerAdd()
customerAdd()
customerAdd()
customerAdd()
customerList()
mNo=int(input("müsteri numarasını giriniz: "))
moneyAdd(mNo)
moneyPull(mNo)
customerFind(mNo)
