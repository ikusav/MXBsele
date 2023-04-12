from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://uat.myxborder.com/admin/login")
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("admin.lokesh@myxborder.com")
driver.find_element(By.ID,"password").send_keys("admin@123")
driver.find_element(By.ID,"emailVerification").click()
driver.find_element(By.ID,"otp").send_keys("1111")
driver.find_element(By.XPATH,'//*[@id="otpVerification"]/div/button').click()