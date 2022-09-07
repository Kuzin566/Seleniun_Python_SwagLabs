
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger

"""Список пользователей"""
user_name = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "Nick_Kuzin"]
"""Список паролей"""
user_password = ["secret_sauce", "secret_sauce", "secret_sauce", "secret_sauce", "my_parol"]


class Login_page(Base):
    url = 'https://www.saucedemo.com'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators:
    locator_user_name = "//input[@id='user-name']"
    locator_user_password = "//*[@id='password']"
    locator_login_button = "//input[@id='login-button']"
    locator_main_word = "//span[@class='title']"

    #Getters:
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_main_word)))

    #Actions:

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user_name : " + user_name)

    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("Input user_password : " + user_password)

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")

    #Metods:
    def avtorization(self):
        Logger.add_start_step(method="avtorization")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name(user_name[0])
        self.input_user_password(user_password[0])
        self.click_login_button()
        self.assert_word(self.get_main_word(), "PRODUCTS")
        Logger.add_end_step(url=self.driver.current_url, method="avtorization")


    # def logout_user(self):
    #     WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id= 'react-burger-menu-btn']"))).click()
    #     time.sleep(2)
    #     WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id= 'logout_sidebar_link']"))).click()
    #     print("Logout")
    #
    #     """Очистка полей ввода логина и пароля"""
    # def cleaning_field(self):
    #     user_name = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    #     user_name.click()
    #     user_name.send_keys(Keys.COMMAND + "a")
    #     user_name.send_keys(Keys.BACKSPACE)
    #     print("Поле User_name очищенно")
    #     user_password = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    #     user_password.click()
    #     user_password.send_keys(Keys.COMMAND + "a")
    #     user_password.send_keys(Keys.BACKSPACE)
    #     print("Поле User_pasword очищенно")




