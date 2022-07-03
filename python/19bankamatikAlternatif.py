#kullanıcı ekle (sınırsız) 
#müsteri no ile müşteri bulma
#bakiye görüntüle
#para çek ve para yatır. 


from asyncio.windows_events import NULL


customers=[]

def customerAdd():
    mNo=int(input("müşteri numarasını giriniz"))
    name=input("müsteri adını giriniz")
    surnamme=input("müşteri soyadını giriniz")
    bakiye=int(input("ilk hesap açılış bakiyesi"))
    customers.append({
        mNo:{
            'name':name,
            'surname':surnamme,
            'bakiye':bakiye
        }
            
    })
def  moneyAdd(mNo):
    
    for c in customers:
        if(mNo in c):
            print(c[mNo])      
            price=int(input("yatırılacak miktarı giriniz: "))
            c[mNo]['bakiye']+=price
            print(f"{price} para hesaba eklendi yeni bakiye {c[mNo]['bakiye']}")
            break

def  moneyPull(mNo):
    
    for c in customers:
        if(mNo in c):
            
            price=int(input("çekilecek para miktarı giriniz: "))
            if(c[mNo]['bakiye']>= price):
                c[mNo]['bakiye']-=price
                print(f"{price} para hesaba eklendi yeni bakiye {c[mNo]['bakiye']}")
                break
            else:
                print(f"bakiyeniz yetersiz en fazla {c[mNo]['bakiye']} çekebilirsiniz")



def customerFind(mNo):
    for c in customers:
        if(mNo in c):
            print(f"{c[mNo]} hesabının sahibi {c[mNo]['name']} {c[mNo]['surname']} kişinin bakiyesi {c[mNo]['bakiye']}")
            






customerAdd()
customerAdd()

mNo=int(input("müsteri numarasını giriniz: "))
moneyAdd(mNo)
moneyPull(mNo)
customerFind(mNo)
