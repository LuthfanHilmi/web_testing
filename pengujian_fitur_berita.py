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
driver.maximize_window()
load_web = WebDriverWait(driver, 20)



def shoot(driver) :
    os.makedirs("hasil_screenshot", exist_ok=True)

    timeFile = time.strftime("%H%M%S")
    screenshot_name = f"screenshot_Akses_fitur_berita_{timeFile}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    driver.save_screenshot(screenshot_path)


try:
    driver.get("https://indonesiaindicator.com/home")
    time.sleep(5)

    news_page = load_web.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link text-white cursor-pointer'][normalize-space()='News']"))
    )
    news_page.click()
    print(":: Melakukan navigasi ke halaman News")
    
    time.sleep(3)
    

    
    openNews = load_web.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".me-2.text-red-500.font-semibold"))
    )
    
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", openNews)
    shoot(driver)
    time.sleep(2)
    openNews.click()
    print(":: Mengakses Recent News Post ")

    tab = driver.window_handles
    driver.switch_to.window(tab[-1])
    time.sleep(7)
    shoot(driver)
    
    print(":: Selesai")
    driver.quit()
except:
    print(f"Terjadi eror")
