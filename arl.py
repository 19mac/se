from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:/Selenium/chromedriver.exe')

driver.get('https://www.saucedemo.com/')


# //*[@id="user-name"]
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')

driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('secret_sauce')

driver.find_element(By.XPATH,'//*[@id="login-button"]').click()

time.sleep(5)

if driver.current_url == "https://www.saucedemo.com/inventory.html":
    print("Login was succuessfull !")
else :
    print("Login failed !")


time.sleep(5)


driver.close()