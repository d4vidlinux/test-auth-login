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

wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_description']"))
)

browser.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()

wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
).click()

wait.until(
    EC.element_to_be_clickable((By.ID, "checkout"))
).click()

first_name = wait.until(
    EC.presence_of_element_located((By.ID, "first-name"))
)

last_name = browser.find_element(By.ID, "last-name")
postal_code = browser.find_element(By.ID, "postal-code")

first_name.send_keys("d4vid")
last_name.send_keys("linux")
postal_code.send_keys("0000")

browser.find_element(By.ID, "continue").click()

finish = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
).click()

input("Press Enter to exit...")
browser.quit()
