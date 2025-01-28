import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
class laptop():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.product = "laptop"
        self.page = 1
        self.item = 1
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #getting all the html code of all pages
        os.makedirs("Data", exist_ok=True)
        for i in range(11):
            self.driver.get(f"https://www.daraz.pk/catalog/?page={self.page}&q={self.product}&spm=a2a0e.tm80335142.search.d_go")
            self.elements = self.driver.find_elements(By.CLASS_NAME, "qmXQo")
            for ele in self.elements:
                with open(f"laptops/{self.product}_{self.item}.html", "w", encoding="utf-8") as f:
                    f.write(ele.get_attribute("outerHTML"))
                    self.item +=1
            time.sleep(2)
            self.page += 1


l = laptop()
    