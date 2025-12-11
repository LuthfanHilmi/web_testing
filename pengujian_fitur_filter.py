from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import os
import random
import time


# setup webdriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_website = WebDriverWait(driver, 20)

#setup exls
wb = Workbook()
ws = wb.active
ws.title("laporan_testing_filter")
ws.append([])


try :
    driver.get('https://indonesiaindicator.com/home')
    #masuk menu careers
    klik_careers = load_website.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='careers']"))
    )
    
    klik_careers.click()
    # print("Berhasil masuk ke bagian careers")

    # filter klik AI Researcher dan All location
    filter1 = load_website.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='AI Researcher']"))
    )
    filterLokasi = load_website.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "option[value='All Location']"))
    )
    
    filter1.click()
    filterLokasi.click()

    time.sleep(60)
    driver.quit()
except: 
    driver.quit()
    exit()