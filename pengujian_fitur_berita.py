# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from openpyxl import Workbook
# import time
# import os


# def save_step(status, deskripsi, driver, laporan_xls):
#     os.makedirs("hasil_screenshot", exist_ok=True)

#     timestamp = time.strftime("%H%M%S")
#     screenshot_name = f"screenshot_{timestamp}.png"
#     screenshot_path = os.path.join("hasil_screenshot", screenshot_name)


#     driver.save_screenshot(screenshot_path) #mengambil gambar

#     # masukkan ke excel
#     laporan_xls.append([status, deskripsi, screenshot_path])


# #setup chromedriver
# servis = Service(executable_path='chromedriver.exe')
# driver = webdriver.Chrome(service=servis)
# load_web = WebDriverWait(driver, 20)


# #setup excl
# wb = Workbook()
# ws = wb.active
# ws.title = "laporan fitur news/berita"
# ws.append(["Status", "Deskripsi", "Screenshot"])


# try:
#     driver.get("https://indonesiaindicator.com/home")
#     news_page = load_web.until(
#          EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='news']"))
#     ).click()

#     save_step("Berhasil", "Berhasil masuk di menu News", driver, ws)
#     time.sleep(3)

#     openNews = load_web.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://www.ntvnews.id/ekonomi/0129559/tiktok-jadi-platform-media-sosial-paling-populer-2024-di-indonesia"]'))
#     )
    
#     save_step("Berhasil", "Berhasil masuk ke salah satu berita", driver, ws)
#     openNews.click()
#     time.sleep(10)
#     wb.save("laporan_testing_berita.xlsx")
#     driver.quit()
# except Exception as e:
#     save_step("Eror", f"Terjadi eror: {str(e)}", driver, ws)
    




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


# Setup Chrome
servis = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)

# Setup Excel
wb = Workbook()
ws = wb.active
ws.title = "laporan fitur news berita"
ws.append(["Status", "Deskripsi", "Screenshot"])

try:
    driver.get("https://indonesiaindicator.com/home")

    # Klik menu News
    news_page = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[navigate='news']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", news_page)
    news_page.click()

    save_step("Berhasil", "Berhasil masuk menu News", driver, ws)
    time.sleep(2)

    # ✨ Klik berita pertama yang muncul (lebih aman daripada href hardcoded)
    openNews = load_web.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='://']")  # semua link berita valid
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", openNews)
    save_step("Berhasil", "Berhasil menemukan link berita", driver, ws)

    openNews.click()
    save_step("Berhasil", "Berhasil membuka halaman berita", driver, ws)

    time.sleep(3)

except Exception as e:
    save_step("Error", f"Terjadi error: {str(e)}", driver, ws)

finally:
    # Selalu simpan laporan
    wb.save("laporan_testing_berita.xlsx")

    # Tutup browser dengan aman
    driver.quit()
