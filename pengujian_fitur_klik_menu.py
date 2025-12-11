from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import os
import random
import time


def save_step(status, deskripsi, driver, laporan_xls):
    os.makedirs("hasil_screenshot", exist_ok=True)

    timestamp = time.strftime("%H%M%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)


    driver.save_screenshot(screenshot_path) #mengambil gambar

    # masukkan ke excel
    laporan_xls.append([status, deskripsi, screenshot_path])



#setup webdriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
driver.set_window_size(360, 800)
load_web = WebDriverWait(driver, 20)


#setup exls
wb = Workbook()
ws = wb.active
ws.title = "laporan_testing_klik_menu"
ws.append(["Status", "Deskripsi", "Screenshot"])


try :
    driver.get("https://indonesiaindicator.com/home")
    
    openMenu = load_web.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'nav-toggle'))
    )
    time.sleep(3)
    openMenu.click()


    openWWA = load_web.until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Who We Are']"))
    )

    openWWA.click()
    save_step("Berhasil", "Berhasil")
    time.sleep(3)

    # openStrategic = load_web.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='strategic-framework']"))
    # ).click()
    # time.sleep(3)

    # openProduct = load_web.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='product']"))
    # ).click()
    # time.sleep(3)

    # openCareers = load_web.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='careers']"))
    # ).click()
    # time.sleep(3)

    # openNews = load_web.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='news']"))
    # ).click()
    # time.sleep(3)

    # openAcademy = load_web.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='i2-academy']"))
    # ).click()
    time.sleep(3)

    
except Exception as e:
    print(f"Error : {e}")
    driver.quit()


