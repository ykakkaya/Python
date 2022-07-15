import requests
import json

class Github():
    def __init__(self):
        self.github_url="https://api.github.com"

    def findUser(self,userName):
        response=requests.get(self.github_url+"/users/"+userName)
        response= json.loads(response.text)
        print(f"kullanıcı adı:  {userName} \nurl adresi: {response['html_url']} \nkullanıcı tam adı: {response['name']} \ntoplam repo sayısı: {response['public_repos']}")

    def getRepos(self,username):
        response=requests.get(self.github_url+"/users/"+userName+"/repos")
        response=json.loads(response.text)
        count=1
        for i in response:
            print(f"{username} kullanıcısına ait repolar: {count}-{i['html_url']}")
            count+=1

    


isStart=True
github=Github()

while(isStart):
    secim=input("1-Find User \n2-Get Repository \n3-Create Repository \n4-Exit \nChoose a item: ")

    if(secim=="1"):
        userName=input("please input User Name:")
        github.findUser(userName)

    elif(secim=="2"):
        userName=input("please input User Name:")
        github.getRepos(userName)
    elif(secim=="3"):
        print("post metodunu kullanarak token yardımıyla oluşturulabilir")
    elif(secim=="4"):
        isStart=False
        print("çıkış işlemi başarılı ")
    else:
        print("yanlış seçim yaptınız.Menüden tekrar bir seçim yapınız")
