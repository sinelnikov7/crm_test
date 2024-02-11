import time
import allure
import pytest
import requests
import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from crm_test.page_objects.clients_page import ClientsPage


@allure.feature('Клиенты')
class TestClients:


    @allure.story('Создание клиентов')
    @allure.severity('Critical')
    def test_create_clients(self, browser_autorized_mozila, access_token):
        """Создание клиентов"""
        page = ClientsPage(browser_autorized_mozila)
        page.driver.get('https://strojregionfilomena.workhere.ru/clients')
        page.get_button_create_client().click()
        input_client_name = page.get_input_client_name()
        input_client_name.send_keys(f'{datetime.date.today()} - 0')
        page.get_button_save_client().click()

    @allure.feature('Клиенты')
    @allure.story('Совпадение статистики статуса активности на вкладке клиенты и в виджете')
    @allure.severity('Normal')
    def test_check_value_vidget_clients(self, browser_autorized_mozila):
        """Проверка значений статистики клиентов в виджете и на вкладке"""
        browser = browser_autorized_mozila
        wait = WebDriverWait(browser, 10)
        browser.get('https://strojregionfilomena.workhere.ru/')
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get('https://strojregionfilomena.workhere.ru/clients')
        interval = ['День', 'Неделя', 'Месяц', 'Весь период']

        for time_stamp in range(1, 5):
            with allure.step(f'Проверка статистики для периода - {interval[time_stamp - 1]}'):
                from_vkladka = []
                from_vidget = []
                for tab in range(0, 2):
                    browser.switch_to.window(browser.window_handles[tab])
                    time_group = browser.find_elements(By.CSS_SELECTOR, '.ant-radio-button-wrapper')
                    time_group[time_stamp - 1].click()
                    time.sleep(3)
                    lists = browser.find_elements(By.CSS_SELECTOR, '.quick-stats__block__2eDvm')
                    if tab == 0:
                        value = from_vidget
                    else:
                        value = from_vkladka
                    for i in lists:
                        value.append(i.text)
                assert from_vidget == from_vkladka
        browser.close()
