from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    url = 'https://toptop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_link_locator = "//header//button[text()='Войти']"

    # Getters

    def get_login_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_link_locator)))


    # Actions

    def click_login_link(self):
        self.get_login_link().click()
        print("Click account icon")



    # Methods

    def open_login_page(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.get_login_link().click()

