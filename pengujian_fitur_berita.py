from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


#setup chromedriver
servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)



def shoot(driver) :
    os.makedirs("hasil_screenshot", exist_ok=True)

    timeFile = time.strftime("%H%M%S")
    screenshot_name = f"Akses_fitur_berita_{timeFile}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    driver.save_screenshot(screenshot_path)


try:
    driver.get("https://indonesiaindicator.com/home")

    news_page = load_web.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link text-white cursor-pointer'][normalize-space()='News']"))
    )
    time.sleep(5)
    news_page.click()
    print(":: Melakukan navigasi ke halaman News")
    
    time.sleep(3)
    shoot(driver)
    time.sleep(3)
    



    openNews = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-100.rounded-lg"))
    )
    time.sleep(1)
    openNews.click()
    print(":: Mengakses Recent News Post ")
    time.sleep(5)
    shoot(driver)
    
    print(":: Selesai")
    driver.quit()
except:
    print(f"Terjadi eror")