from asyncore import read
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver =webdriver.Chrome(executable_path='/Users/hmm/Downloads/chromedriver')
driver.get("https://www.saucedemo.com")

with open('data.csv','r')as file:
    reader=list(csv.reader(file))

for i in range(1,len(reader)):
    username=reader[i][0]
    password=reader[i][1]
    driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="login-button"]').click()
    if driver.current_url=='https://www.saucedemo.com/inventory.html':
        print(f"Username:  {username} | Password {password}\nResult pass")
        driver.get("https://www.saucedemo.com")
    else:
        print(f"Username:  {username} | Password {password}\nResult fail")
 

driver.close()