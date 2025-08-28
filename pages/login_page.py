from dotenv import load_dotenv, dotenv_values
import os

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    url = 'https://toptop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_button_locator = "//header//button[text()='Войти']"
    email_input_locator = "//input[@name='email']"
    password_input_locator = "//input[@name='password']"
    confirm_login_button_locator = "//button[@type='submit']"
    cabinet_button_locator = "//header//button[text()='Кабинет']"

    # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_locator)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_input_locator)))

    def get_password_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_input_locator)))


    def get_confirm_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_login_button_locator)))

    def get_cabinet_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cabinet_button_locator)))

    # Actions
    def click_login_link(self):
        self.get_login_button().click()
        print("Click account icon")



    def fill_email_input(self):
        self.get_email_input().send_keys(str(os.getenv("EMAIL")))
        print("Fill email input field")


    def fill_password_input(self):
        self.get_password_input().send_keys(str(os.getenv("PASSWORD")))
        print("Fill password input field")

    def click_confirm_login_button(self):
        self.get_confirm_login_button().click()
        print("Click login button")

    # Methods
    def login(self):
        self.driver.get(self.url)
        self.get_login_button().click()
        self.fill_email_input()
        self.fill_password_input()
        self.click_confirm_login_button()
        self.assert_word(self.get_cabinet_button(), 'КАБИНЕТ')

