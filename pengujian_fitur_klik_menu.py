from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time
import os

#setup webdriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
driver.set_window_size(360, 800)
load_web = WebDriverWait(driver, 20)

#setup xls
wb = Workbook()
ws = wb.active
ws.title = "Hasil tes klik menu"
ws.append(["Status", "Deskripsi", "Screenshot"])


def save_step(status, deskripsi, driver, laporan_xls):
    os.makedirs("hasil_screenshot", exist_ok=True)

    timestamp = time.strftime("%H%M%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    
    driver.save_screenshot(screenshot_path)

    
    laporan_xls.append([status, deskripsi, screenshot_path])


def open_menu():
    btn_menu = load_web.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "nav-toggle"))
    )
    btn_menu.click()
    time.sleep(1)


driver.get("https://indonesiaindicator.com/home")
time.sleep(2)

#letak class 
submenus = [
    "#mobile-menu a[navigate='who-we-are']",
    "#mobile-menu a[navigate='strategic-framework']",
    "#mobile-menu a[navigate='product']",
    "#mobile-menu a[navigate='careers']",
    "#mobile-menu a[navigate='news']",
    "#mobile-menu a[navigate='i2-academy']"
]
#nama submenu
nama_submenu = [
    "Who We Are",
    "Strategic Framework",
    "Product",
    "Careers",
    "News",
    "i2 Academy"
]

for selector, nama in zip(submenus, nama_submenu):

    try:
        open_menu()

        submenu = load_web.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )

        # old_url = driver.current_url
        submenu.click()

        time.sleep(1)
        save_step("Berhasil", f"Berhasil masuk ke menu {nama}", driver, ws)

    except Exception as e:
        print(f"Error saat klik {nama}: {e}")
        save_step("Error", f"Gagal masuk ke menu {nama}: {e}", driver, ws)
        continue
    finally:
        wb.save("laporan_testing_menu.xlsx")