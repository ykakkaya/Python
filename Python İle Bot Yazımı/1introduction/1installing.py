
from selenium import webdriver
import time

driver=webdriver.Chrome()
url="https://ykakkaya.com"
#verilen url adresine gider
driver.get(url)
#sayfayı tam ekran yapar
driver.maximize_window()
#verilen isimde ekran görüntüsü alır
driver.save_screenshot("ykakkayaHomePage.png")
#belirtilen saniye kadar bekler
time.sleep(3)
#gidilen sayfa başlığını alır
print(driver.title)

url2="https://github.com/ykakkaya"
driver.get(url=url2)
driver.maximize_window()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
if("ykakkaya" in driver.title):
    driver.save_screenshot("githubEkran.png")
time.sleep(2)
driver.close()