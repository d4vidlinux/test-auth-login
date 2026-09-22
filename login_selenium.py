#!/usr/bin/env python3

from functions import *


def main():
    openWindow("https://saucedemo.com")

    login("standard_user", "secret_sauce")

    addItemToCart("//div[text()='Sauce Labs Backpack']")

    finish()

#-------------------------------------------------

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
    browser.quit()
