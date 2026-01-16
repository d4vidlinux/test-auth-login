from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Driver
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

#Connect
browser.get("https://saucedemo.com")

#Maximize_window
browser.maximize_window()

#Auth fields
username = wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
)
password = wait.until(
    EC.presence_of_element_located((By.ID, "password"))
)

#Login button
btn_login = wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)

# send_keys()
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click
btn_login.click()

input("Press Enter to exit...")
browser.quit()