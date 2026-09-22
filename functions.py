from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


global browser
global wait

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def openWindow(website):
    browser.get(website)
    browser.maximize_window()


def testLoginSuccessful(xpath):
    test = wait.until(
    EC.presence_of_element_located((By.XPATH, xpath))
    )
    assert test, "Error in Login"

def login_successful(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        testLoginSuccessful("//div[@class='inventory_item_description']")
    return wrapper


@login_successful
def login(user, password):
    #Auth fields
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(user)

    wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    ).send_keys(password)

    #Login button
    btn_login = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()



def checkout(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
        ).click()

        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    return wrapper


@checkout
def addItemToCart(xpath_item):
    browser.find_element(By.XPATH, xpath_item).click()
    wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart"))
    ).click()


def finish(fname="d4vid", lname="linux", pcode="0000"):

    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    last_name = browser.find_element(By.ID, "last-name")
    postal_code = browser.find_element(By.ID, "postal-code")

    first_name.send_keys(fname)
    last_name.send_keys(lname)
    postal_code.send_keys(pcode)

    browser.find_element(By.ID, "continue").click()

    finish = wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()






             