import time
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.common.by import By

from seleniumwire import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from fake_useragent import UserAgent
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

proxies = {'proxy': {
    'http': "socks5://b2Py87:k9CgGb@45.143.246.231:8000",
    'https': "socks5://b2Py87:k9CgGb@45.143.246.231:8000",
}}

def test_link_about():
    load_dotenv()
    ua = UserAgent()
    options_chrome = webdriver.ChromeOptions()
    options_chrome.page_load_strategy = 'eager' # Без этой настройки скрипты работают медленнее
    options_chrome.add_argument('--start-maximized') # Максимальный для устройства размер окна
    options_chrome.add_argument('--disable-notifications') # Убирает уведомления
    options_chrome.add_experimental_option("excludeSwitches", ["enable-logging"])
    options_chrome.add_experimental_option("excludeSwitches", ["enable-automation"])
    options_chrome.add_experimental_option("useAutomationExtension", False)
    options_chrome.add_argument("--disable-blink-features=AutomationControlled")
    options_chrome.add_argument(f'user-agent={ua.chrome}')

    with webdriver.Chrome(options=options_chrome, seleniumwire_options=proxies) as browser:
        lp = LoginPage(browser)
        lp.login()
        time.sleep(5)
        print(lp.get_current_url())
