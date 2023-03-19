import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


time_m = '2023-03-19 09:00:00'

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--ignore-ssl-errors')
chromeOptions.add_argument("--remote-debugging-port=0") 

browser = webdriver.Chrome(executable_path="C:/Users/Pinhan Chen/AppData/Local/Google/Chrome/Application/chromedriver.exe",chrome_options=chromeOptions)

browser.get('https://www.jd.com/?country=China')
time.sleep(3)

browser.find_element(By.LINK_TEXT,'你好，请登录').click()
print('请扫码')
time.sleep(10)

browser.get('https://cart.jd.com/cart_index')
time.sleep(3)


while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    print(now)

    if now > time_m:
        while True:
            if browser.find_element(By.CLASS_NAME, "jdcheckbox"):
                browser.find_element(By.CLASS_NAME, "jdcheckbox").click()
                break
        time.sleep(0.3)
        while True:

            if browser.find_element(By.LINK_TEXT,'去结算'):
                browser.find_element(By.LINK_TEXT,'去结算').click()
                print('结算提交成功')
                break
            
        while True:
            try:
                if browser.find_element(By.LINK_TEXT,'结算'):
                    browser.find_element(By.LINK_TEXT,'结算').click()
                    print('提交成功')
            except:
                pass
