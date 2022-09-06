import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

"Список локаторов Названий"
locator_product_name = ["//*[@id='item_4_title_link']/div", "//*[@id='item_0_title_link']/div", "//*[@id='item_1_title_link']/div", "//*[@id='item_5_title_link']/div", "//*[@id='item_2_title_link']/div", "//*[@id='item_3_title_link']/div"]
"""Список локаторов цены"""
locator_price_product = ["//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"]
"Список локаторов Add_to cart"
locator_select_product = ["//*[@id='add-to-cart-sauce-labs-backpack']", "//*[@id='add-to-cart-sauce-labs-bike-light']", "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']", "//*[@id='add-to-cart-sauce-labs-fleece-jacket']", "//*[@id='add-to-cart-sauce-labs-onesie']", "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"]



class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    locator_cart_button = "//*[@id='shopping_cart_container']/a"   #локатор кнопки корзина
    locator_menu_button = "// button[ @ id = 'react-burger-menu-btn']"
    locator_about_button = "//a[@id = 'about_sidebar_link']"

    #Getters
    def get_select_product(self,):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_select_product[int(self.number_product) -1]))))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_cart_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_menu_button)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_about_button)))
    #Actions

    def click_add_cart_button(self, number):
        self.number_product = number
        self.get_select_product().click()
        print("Click add to cart button")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart button")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click Menu button")

    def click_about_button(self):
        self.get_about_button().click()
        print("Click About button")

    #Metods
    def select_product(self, numbers_product):
        self.number_product = numbers_product
        self.get_current_url()
        self.click_add_cart_button(self.number_product)
        self.click_cart_button()


    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.get_current_url()
        self.assert_url("https://saucelabs.com/")







