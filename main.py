import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


time_m = '2023-03-20 15:55:00'

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--ignore-ssl-errors')
chromeOptions.add_argument("--remote-debugging-port=0") 
chromeOptions.add_argument("start-maximized")

browser = webdriver.Chrome(executable_path="C:/Users/cph56/AppData/Local/Google/Chrome/chromedriver.exe",chrome_options=chromeOptions)

browser.get('https://www.jd.com/?country=China')
time.sleep(3)

browser.find_element(By.LINK_TEXT,'你好，请登录').click()
print('请扫码')
time.sleep(10)

browser.get('https://cart.jd.com/cart_index')
time.sleep(3)
XPATH = '//*[@id="cart-body"]/div[2]/div[3]/div[1]/div/input'

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    print(now)

    if now > time_m:
        time.sleep(0.2)
        while 1==1:
            try:
                # nowb = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                if browser.find_element(By.XPATH, XPATH).get_attribute("clstag")[-1] == str(0):
                    
                    
                    
                    # nowa = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    # print(nowb,nowa)
                    browser.find_element(By.CLASS_NAME, "jdcheckbox").click()
                    
                    break
                    
                        
                
            except:
                pass

        
        while 1==1:

            
            try:   
                if browser.find_element(By.XPATH, XPATH).get_attribute("clstag")[-1] == str(1):
                    # nowc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    browser.find_element(By.XPATH,'//*[@id="cart-body"]/div[2]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a/b').click()
                    print('结算提交成功')
                    # print(nowc)
                    break
            except:
                pass
        

            # if browser.find_element(By.LINK_TEXT,'去结算'):
            #         browser.find_element(By.LINK_TEXT,'去结算').click()
            #         print('结算提交成功')

        while True: 
            try:    
                if browser.find_element(By.XPATH,'//*[@id="order-submit"]/b'):
                    browser.find_element(By.XPATH,'//*[@id="order-submit"]/b').click()
                    print('提交成功') 
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                    break   
            except:
                pass
        
        
