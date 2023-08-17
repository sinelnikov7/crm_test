import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import imaplib
import email
import time




@pytest.fixture(scope='session')
def chrome_driver_wont_close():
    chrome_driver_wont_close = webdriver.Chrome(service=ChromeService(executable_path='C:/chromedriver/chromedriver'))
    return chrome_driver_wont_close

@pytest.fixture(scope='session')
def fox_driver_wont_close():
    fox_driver_wont_close = webdriver.Chrome(service=ChromeService(executable_path='C:/chromedriver/chromedriver'))
    return fox_driver_wont_close


@pytest.fixture
def chrome_driver_will_close():
    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    chrome_driver_will_close = webdriver.Firefox()

    return chrome_driver_will_close


@pytest.fixture
def fox_driver_will_close():
    # op = webdriver.FirefoxOptions()
    # op.add_argument('--headless')
    # fos_driver_will_close = webdriver.Firefox(options=op)
    fox_driver_will_close = webdriver.Firefox()
    return fox_driver_will_close


@pytest.fixture(scope='session')
def fox_driver_wont_close():
    # op = webdriver.FirefoxOptions()
    # op.add_argument('--headless')
    # fos_driver_will_close = webdriver.Firefox(options=op)
    fox_driver_wont_close = webdriver.Firefox()
    return fox_driver_wont_close

@pytest.fixture(scope='session')
def access_token():
    data = {"user": "admin", "password": "testtest1"}
    response = requests.post('https://strojregionfilomena.workhere.ru/api/auth/login', data=data).json()
    access_token = response['data']['token']
    return access_token

@pytest.fixture(scope='session')
def browser_autorized_mozila():
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    # browser_autorized_mozila = webdriver.Firefox(options=op)
    browser_autorized_mozila = webdriver.Firefox()
    browser_autorized_mozila.implicitly_wait(10)
    browser_autorized_mozila.get('https://strojregionfilomena.workhere.ru/clients')
    user = browser_autorized_mozila.find_element(By.ID, "auth-form-login_user")
    password = browser_autorized_mozila.find_element(By.ID, 'auth-form-login_password')
    login_button = browser_autorized_mozila.find_element(By.CSS_SELECTOR, '.ant-btn-block')
    user.send_keys('admin')
    password.send_keys('testtest1')
    login_button.click()
    time.sleep(5)
    return browser_autorized_mozila
