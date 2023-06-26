import pytest
from selenium import webdriver
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


@pytest.fixture
def chrome_driver_will_close():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    chrome_driver_will_close = webdriver.Chrome(service=ChromeService(executable_path='C:/chromedriver/chromedriver'), options=op)

    return chrome_driver_will_close


@pytest.fixture
def fox_driver_will_close():
    # op = webdriver.FirefoxOptions()
    # op.add_argument('--headless')
    # fos_driver_will_close = webdriver.Firefox(options=op)
    fox_driver_will_close = webdriver.Firefox()
    return fox_driver_will_close


# print(get_key())
