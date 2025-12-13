from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
# from selenium.webdriver.common.action_chains import ActionChains
import os
import time



servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)



wb = Workbook()
ws = wb.active
ws.title = "Hasil tes filter"
ws.append(["Status", "Deskripsi", "Screenshot"])



def save_step(status, deskripsi, driver, laporan_xls):
    os.makedirs("hasil_screenshot", exist_ok=True)

    timestamp = time.strftime("%H%M%S")
    screenshot_name = f"screenshot_fitur_Filter_{timestamp}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    driver.save_screenshot(screenshot_path) 
    laporan_xls.append([status, deskripsi, screenshot_path])





try :
    driver.get('https://indonesiaindicator.com/home')
    time.sleep(5)

    klik_careers = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='max-w-7xl mx-auto'] li:nth-child(5) a:nth-child(1)"))
    )
    time.sleep(3)
    klik_careers.click()
    time.sleep(5)
    save_step("Berhasil", "Melakukan navigasi ke halaman careers", driver, ws)



    elemenFilterPosition = driver.find_element(By.CSS_SELECTOR, "div[class='my-12 mx-auto grid gap-4 items-center flex grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5'] div:nth-child(2) select:nth-child(1)")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elemenFilterPosition)
    time.sleep(1)
    elemenFilterPosition.click()
    save_step("Berhasil", "Mekakukan klik pada menu All Position", driver, ws)
    time.sleep(2)
    selectElement1 = Select(elemenFilterPosition).select_by_visible_text("Data Analyst")
    time.sleep(1)
    save_step("Berhasil", "Memilih menu Data Analyst", driver, ws)


    elementFilterLocation = driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) select:nth-child(1)")
    time.sleep(1)
    elementFilterLocation.click()
    save_step("Berhasil", "Mekakukan klik pada menu Location", driver, ws)
    time.sleep(2)
    selectElement2 = Select(elementFilterLocation).select_by_visible_text("South Tangerang")
    time.sleep(1)
    save_step("Berhasil", "Memilih menu South Tangerang", driver, ws)
    time.sleep(1)
    
    wb.save("Laporan_testing_filter_sort.xlsx")
    driver.quit()
except: 
    driver.quit()
    exit()