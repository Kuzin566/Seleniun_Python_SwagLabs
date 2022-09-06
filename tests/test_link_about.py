import time
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.client_information_page import Client_information_page
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page


def test_link_about():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/Users/viktoria27vika27/PycharmProjects/resource/chromedriver', chrome_options=options)

    print("Start")
    login = Login_page(driver)
    login.avtorization()

    mp = Main_page(driver)
    mp.select_menu_about()
    driver.close()
