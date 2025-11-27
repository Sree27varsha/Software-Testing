from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.maximize_window()
with open("C:/Users/Dell/Desktop/Software Testing/details.csv",newline='')as file:
    reader=csv.DictReader(file)
    for row in reader:
        username=row["username"]
        password=row["password"]
        print(f"Testing: {username}/{password}")
        driver.find_element(By.CLASS_NAME,"username").clear()
        driver.find_element(By.CLASS_NAME,"password").clear()
        driver.find_element(By.CLASS_NAME,"username").send_keys(username)
        driver.find_element(By.CLASS_NAME,"password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "div[data-testid='login-button']")

        time.sleep(20)
        if "Security" in driver.page_source:
            print("Login failed (security check triggered).")
        else:
            print("Login successful.")
driver.quit()