import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base



class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators:
    locator_first_name = "//*[@id='first-name']"
    locator_last_name= "//*[@id='last-name']"
    locator_postal_code = "//*[@id='postal-code']"
    locator_continue_button = "//*[@id='continue']"

    #Getters:
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_continue_button)))

    #Actions:

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name : " + first_name)

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name : " + last_name)

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal_code : " + postal_code)

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click CONTINUE button")

    #Metods:
    def input_client_information(self):
        self.get_current_url()
        self.input_first_name("Nick")
        self.input_last_name("Kuzin")
        self.input_postal_code("426000")
        self.click_continue_button()








