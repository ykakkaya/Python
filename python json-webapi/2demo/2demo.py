import json
import os

class User:
    def __init__(self,userName,password,email):
        self.userName=userName
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUsers={}


        #load users from .json file
        self.loadUsers()


    def loadUsers(self):
        if(os.path.exists("users.json")):
            with open("users.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(userName=user["userName"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)


    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print(f"{user.userName} kullanıcısı oluşturuldu ")


    def login(self,userName,password):
        for user in self.users:
            if user.userName ==userName and user.password==password :
                self.isLoggedIn=True
                self.currentUsers=user
                print("login yapıldı")
                break

    def logout(self):
        self.isLoggedIn=False
        self.currentUsers={}
        print("çıkış işlemi yapıldı")

    def identity(self):
        if(self.isLoggedIn):
            print(f"userName {self.currentUsers.userName}")
        else:
            print("kullanıcı giriş yapmadı")
        


    def saveToFile(self):
        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))



        with open("users.json","w") as file:
            json.dump(list,file)



repository=UserRepository()
while True:
    print("MENÜ".center(50,"*"))
    secim=int(input("1-REGİSTER\n2-LOGİN\n3-LOGOUT\n4-IDENTITY\n5-EXIT\nSEÇİMİNİZİ YAPINIZ: "))

    if(secim==1):

        if(repository.isLoggedIn):
            print("zaten giriş yapıldı")
        else:
            userName=input("kullanıcı adını giriniz: ")
            password=input("parolanızı giriniz: ")
            email=input("E-mail bilginizi giriniz: ")

            user=User(userName=userName,password=password,email=email)
            repository.register(user)
            print(repository.users)


        
    elif(secim==2):
        userName=input("kullanıcı adını giriniz: ")
        password=input("parolanızı giriniz: ")
        repository.login(userName,password)

    elif(secim==3):
        repository.logout()
    elif(secim==4):
        repository.identity()
    elif(secim==5):
        break
    elif(secim==6):
        print("HATALI GİRİŞ LÜTFEN TEKRAR DENEYİNİZ")