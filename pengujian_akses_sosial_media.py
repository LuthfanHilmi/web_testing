from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
import time
import os


servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)
act = ActionChains(driver)


wb = Workbook()
ws = wb.active
ws.title = "laporan akses sosmed"
ws.append(["Status, Deskripsi, Screenshot"])

def save_step(status, deskripsi, driver, laporan) :
    os.makedirs("hasil_screenshot", exist_ok=True)

    timeFile = time.strftime("%H%M%S%")
    screenshot_name = f"aksesSosmed{timeFile}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    driver.save_screenshot(screenshot_path)
    laporan.append([status, deskripsi, screenshot_path])



try:
    driver.get("https://indonesiaindicator.com/home")
    time.sleep(10)


    instagram = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='py-5 px-10'] a:nth-child(1) svg"))
    )
    assert instagram.is_displayed()
    act.move_to_element(instagram).send_keys(Keys.END).perform()
    time.sleep(3)
    save_step("Berhasil", "Scroll bagiann bawah untuk klik instagram", driver, ws)

    
    time.sleep(5)
    instagram.click()
    time.sleep(10)
    save_step("Berhasil", "Berhasil masuk ke instagram", driver, ws)
    wb.save("laporan_akses_sosmed.xlsx")
    driver.quit()
except:
    print(f"Terjadi eror")



