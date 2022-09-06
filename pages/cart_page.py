import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators:

    locator_checkout_button = "//button[@id = 'checkout']"   #локатор кнопки Checkout

    #Getters:

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_checkout_button)))


    #Actions:

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click CHECKOUT button")



    #Metods:
    def product_confirmation(self):  #подтверждение товара
        self.get_current_url()
        self.click_checkout_button()







