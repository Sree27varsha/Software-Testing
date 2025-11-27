from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500);")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-300);")
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollheight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0,0);")
time.sleep(5)
print("scrolling complete successfully.")
driver.quit()