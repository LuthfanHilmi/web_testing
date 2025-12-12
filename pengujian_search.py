from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time
import os


def save_step(status, deskripsi, driver, laporan_xls):
    os.makedirs("hasil_screenshot", exist_ok=True)

    timestamp = time.strftime("%H%M%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)


    driver.save_screenshot(screenshot_path) 
    
    laporan_xls.append([status, deskripsi, screenshot_path])

    

#setup chromedriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)

#setup excl
wb = Workbook()
ws = wb.active
ws.title = "Hasil tes fitur search"
ws.append(["Status", "Deskripsi", "Screenshot"])


try:
    driver.get("https://indonesiaindicator.com/home")

    careers = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='careers']"))
    )
    careers.click()
    save_step("BERHASIL", "Membuka halaman Careers", driver, ws)

    search1 = load_web.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "searchbar-input"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search1)

    keyword = "Data Engineer"
    search1.send_keys(keyword)
    save_step("BERHASIL", f"Berhasil melakukan input {keyword}", driver, ws)

    time.sleep(2)

    search2 = load_web.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "searchbar-input"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search2)

    search1.clear()
    keyword = "cyber"
    search2.send_keys(keyword)
    save_step("GAGAL", f"inputan {keyword} tidak ditemukan", driver, ws)
    time.sleep(1)

    wb.save("laporan_testing_search.xlsx")
    driver.quit()

except Exception as e:
    save_step("Eror", f"Terjadi eror: {str(e)}", driver, ws)

