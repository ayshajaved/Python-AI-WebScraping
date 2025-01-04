import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Lanching Chrome...!")
    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        driver.get(website)
        print("Page loaded!")
        html = driver.page_source
        time.sleep(10)

        return html
    except Exception as e:
        print(e)
        return None
    finally:
        driver.quit()
        