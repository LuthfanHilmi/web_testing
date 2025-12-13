from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


servis = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=servis)
load_web = WebDriverWait(driver, 20)
act = ActionChains(driver)


def shoot(driver) :
    os.makedirs("hasil_screenshot", exist_ok=True)

    timeFile = time.strftime("%H%M%S")
    screenshot_name = f"screenshot_Akses_sosmed_{timeFile}.png"
    screenshot_path = os.path.join("hasil_screenshot", screenshot_name)

    driver.save_screenshot(screenshot_path)



try:
    driver.get("https://indonesiaindicator.com/home")
    time.sleep(5)
    print(":: Berhasil akses website Indonesia Indicator")
    



    instagram = load_web.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='py-5 px-10'] a:nth-child(1) svg"))
    )
    assert instagram.is_displayed()
    act.move_to_element(instagram).send_keys(Keys.END).perform()
    print(":: Melakukan akses ke instagram PT Indonesia Indicator")

    time.sleep(5)
    shoot(driver)

    
    instagram.click()
    
    tab = driver.window_handles
    driver.switch_to.window(tab[-1])
    time.sleep(15)
    shoot(driver)
    time.sleep(1)

    print(":: Selesai")
    driver.quit()
except:
    print(f":: Terjadi eror")



