from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time
import os

#setup chromedriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)


try:
    driver.get("https://indonesiaindicator.com/news")
    openNews = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://www.ntvnews.id/ekonomi/0129559/tiktok-jadi-platform-media-sosial-paling-populer-2024-di-indonesia"]'))
    )
    openNews.click()
    time.sleep(20)
except Exception as e:
    print(f"Error : {e}")
    