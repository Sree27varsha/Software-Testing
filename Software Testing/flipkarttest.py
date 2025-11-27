from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Track test status
test_passed = True
error_messages = []

# 1. Open Flipkart homepage
try:
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    time.sleep(3)
except:
    print("❌ Error: Unable to open Flipkart homepage")
    test_passed = False
    error_messages.append("homepage")

# 2. Close initial login popup if appears
try:
    close_btn = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_btn.click()
    time.sleep(2)
except:
    pass  # No popup is fine

# 3. Click on Login button
try:
    login_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
    login_btn.click()
    time.sleep(3)
except:
    print("❌ Error: Login button")
    test_passed = False
    error_messages.append("login button")

# 4. Enter login details
try:
    username = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    username.send_keys("fakeuser123@gmail.com")  # Invalid Email
    password.send_keys("wrongPassword123")       # Invalid Password
    password.send_keys(Keys.ENTER)
    time.sleep(4)

    # Check for error message
    try:
        error_msg = driver.find_element(By.XPATH, "//span[contains(text(),'Please enter valid')]")
        print("Login Test Result: ", error_msg.text)
        test_passed = False
        error_messages.append("login credentials")
    except:
        print("Login Test Result: No errors")
except:
    print("❌ Error: Login fields not found")
    test_passed = False
    error_messages.append("login fields")

# 5. Search for a product
try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("mobile")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
except:
    print("❌ Error: Search box")
    test_passed = False
    error_messages.append("search box")

# 6. Select first product
try:
    first_product = driver.find_element(By.XPATH, "(//a[@class='s1Q9rs' or contains(@class,'IRpwTa')])[1]")
    first_product.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])  # Switch to new tab
except:
    print("❌ Error: Selecting first product")
    test_passed = False
    error_messages.append("product selection")

# 7. Add to cart
try:
    add_to_cart = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart.click()
    print("Cart Test Result: Product added successfully")
except:
    print("❌ Error: Add to cart")
    test_passed = False
    error_messages.append("add to cart")

time.sleep(3)

# 8. Proceed to checkout
try:
    place_order = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
    place_order.click()
    print("Checkout Test Result: Checkout flow initiated")
except:
    print("❌ Error: Checkout")
    test_passed = False
    error_messages.append("checkout")

time.sleep(5)

# 9. Final Test Result
if test_passed:
    print("✅ No errors, testing completed successfully.")
else:
    print("❌ Some errors occurred in:", ", ".join(error_messages))

# 10. Close browser
driver.quit()
