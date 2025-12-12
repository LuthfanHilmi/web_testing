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


# setup excl
wb = Workbook()
ws = wb.active
ws.title = "laporan fitur barita"
ws.append(["Status", "Deskripsi", "Screenshot"])


def save_step(status, deskripsi, driver, laporan) :
    os.makedirs("hasil_screenshot", exist_ok=True)
    
    timesfile = time.strftime("%H%M%S")
    screenshot_name = f"fiturBerita{timesfile}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    driver.save_screenshot(screenshot_path)
    laporan.append([status, deskripsi, screenshot_path])


try:
    driver.get("https://indonesiaindicator.com/home")

    news_page = load_web.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link text-white cursor-pointer'][normalize-space()='News']"))
    )
    time.sleep(5)
    news_page.click()
    time.sleep(2)
    save_step("Berhasil", "Berhasil masuk ke halaman berita", driver, ws)



    openNews = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-100.rounded-lg"))
    )
    time.sleep(1)
    openNews.click()
    time.sleep(5)
    
    wb.save("Laporan_tesing_berita.xlsx")
    driver.quit()
except:
    print(f"Terjadi eror")