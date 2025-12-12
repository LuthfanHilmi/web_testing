from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random
import time


# setup webdriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_website = WebDriverWait(driver, 20)



try :
    driver.get('https://indonesiaindicator.com/home')
    time.sleep(5)
    klik_careers = load_website.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='my-12 mx-auto grid gap-4 items-center flex grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5'] div:nth-child(2) select:nth-child(1)"))
    )
    time.sleep(5)
    klik_careers.click()
    time.sleep(5)
except: 
    driver.quit()
    exit()