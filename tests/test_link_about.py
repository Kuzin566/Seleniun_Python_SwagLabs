from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page



def test_link_about():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='D:\\ProjectPCh\\resourse\\chromedriver.exe', chrome_options=options)

    print("Start")
    login = Login_page(driver)
    login.avtorization()

    mp = Main_page(driver)
    mp.select_menu_about()
    driver.close()
