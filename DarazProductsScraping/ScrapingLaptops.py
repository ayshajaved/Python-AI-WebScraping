import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
class ScrapingLaptops():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.product = "laptop"
        self.page = 1
        self.item = 1
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        os.makedirs("Data", exist_ok=True)  #making directory for the data of laptops to be stored in html
        self.scrape()
    def scrape(self):
        #getting all the html code of all pages
        for i in range(11):                #Scrapiing 10 pages each having approx 40 laptops
            self.driver.get(f"https://www.daraz.pk/catalog/?page={self.page}&q={self.product}&spm=a2a0e.tm80335142.search.d_go")
            self.elements = self.driver.find_elements(By.CLASS_NAME, "qmXQo")
            for ele in self.elements:
                with open(f"Data/{self.product}_{self.item}.html", "w", encoding="utf-8") as f:
                    f.write(ele.get_attribute("outerHTML"))
                    self.item +=1
            time.sleep(2)
            self.page += 1
l = ScrapingLaptops()
    