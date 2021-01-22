from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from store_credentials import store, viewdata
from time import sleep


def get_driver():
    x = webdriver.Chrome('/home/dev/Desktop/chromedriver')
    return x

def search_input(platform):
    """
        This function takes the platform name as input and appends login to it and searches
        it on www.google.com search box
    """
    driver = get_driver()
    site = platform + ' ' + 'login'
    driver.maximize_window()
    sleep(2)
    driver.get('https://www.google.com/')
    sleep(2)
    driver.find_element_by_css_selector("input[name='q']").send_keys(site)
    sleep(2)
    driver.find_element_by_css_selector("input[name='btnK']").click()


# <input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwiMprb6vqzuAhVZcCsKHZ_1DeYQ39UDCAQ">
def login():
    print("Reached login Function")

    # Taking Platform input from user and searching for the credentials in .txt file
    platform = input('Enter the platform on which you want me to login : ').lower()
    credentials = viewdata(platform)
    username = credentials[0]
    password = credentials[1]
    driver = get_driver()

    # Searching the platform on google.com with login appended
    search_input(platform)
    # sleep(20)

    # Click On the very first search result of the google search
    actions.send_keys(Keys.TAB * 18)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Asking the user for to exit out the program
    choice = input("Do you want to exit out if yes enter 'y' otherwise enter any other character : ")
    if choice == 'y':
        print("Exiting Out..")


if __name__ == '__main__':
    print('''      Welcome to AutoLogin System     ''')
    print('''
                       1. Login
                       2. Store Login Details
        ''')
    n = int(input("Enter your choice : "))
    if n == 1:
        login()
    elif n == 2:
        store()
    else:
        print("Please do enter the valid choice")

