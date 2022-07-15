import imp
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#github üzerinden python u aratıp çıkan sayfadaki repoları listeleme işlemi

driver=webdriver.Chrome()
url="https://github.com"
driver.get(url=url)
driver.maximize_window()
time.sleep(3)

searchInput=driver.find_element(By.XPATH,"//input[@type='text']")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
result=driver.find_elements(By.XPATH,"//a[@class='v-align-middle']")
count=1
for item in result:
    print(f"{count}-{item.text}")
    count+=1

driver.close()


