from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#bilgileri alınan bir kullanıcının takip ettiği kullanıcılar

class GitHub():

    def __init__(self,userName,password):
        self.driver=webdriver.Chrome()
        self.userName=userName
        self.password=password

    def FirtStep(self):
        url="https://github.com"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)
        signIn=self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a")
        signIn.click()
        time.sleep(2)

    def SecondStep(self):
        nameInput=self.driver.find_element(By.XPATH,"//*[@id='login_field']")
        nameInput.send_keys(self.userName)
        time.sleep(1)
        passwordInput=self.driver.find_element(By.XPATH,"//*[@id='password']")
        passwordInput.send_keys(self.password)
        time.sleep(1)
        submitClick=self.driver.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[12]")
        submitClick.click()
        time.sleep(3)

    def ThirthStep(self):
        avatar=self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details/summary/img")
        avatar.click()
        time.sleep(1)
        profil=self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details/details-menu/a[1]")
        profil.click()
        time.sleep(2)
        following=self.driver.find_element(By.XPATH,"//*[@id='js-pjax-container']/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[2]")
        following.click()
        time.sleep(2)

    def FourthStep(self):
        list=self.driver.find_elements(By.XPATH,"//span[@class='f4 Link--primary']")
        count=1
        
        print("TAKİP ETTİKLERİM")
        for item in list:
            print(f"{count}-{item.text}")
            count+=1
        time.sleep(3)
        self.driver.close()


userName=input("kullanıcı adı: ")
password= input("password: ")
git=GitHub(userName,password)
git.FirtStep()
git.SecondStep()
git.ThirthStep()
git.FourthStep()