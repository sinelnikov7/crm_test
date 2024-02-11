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
from crm_test.services.mail import get_key, get_new_password
from crm_test.page_objects.auth_page import AuthPage

#
# @allure.feature('Авторизация')
# class TestAuth:
#
#     @allure.story('Авторизация с невалидными данными')
#     @allure.severity('Normal')
#     def test_auth_with_invalid_data(self, fox_driver_will_close):
#         """Авторизация с невалидными данными"""
#         page = AuthPage(fox_driver_will_close)
#         data = [
#             {'login': 'admins', 'password': 'testtest1', 'description': 'Невалидный логин'},
#             {'login': 'admin', 'password': 'testtest', 'description': 'Невалидный пароль'},
#             {'login': 'admins', 'password': 'testtest', 'description': 'Невалидный логин и пароль'}
#         ]
#
#         with allure.step('Наличие поля "Логин"'):
#             user = page.get_input_login()
#         with allure.step('Наличие поля "Пароль"'):
#             password = page.get_input_password()
#         with allure.step('Наличие кнопки "Войти"'):
#             login_button = page.get_button_login()
#         for value in data:
#             with allure.step('Заполнение поля "Логин"'):
#                 user.send_keys(value.get('login'))
#             with allure.step('Заполнение поля "Пароль"'):
#                 password.send_keys(value.get('password'))
#             with allure.step(f'Авторизация с {value.get("description")}'):
#                 try:
#                     WebDriverWait(page, 5).until(EC.element_to_be_clickable(login_button))
#                     login_button.click()
#                     message = page.driver.find_element(By.CSS_SELECTOR, '.auth-forms-content-fields-message__hIBT7').text
#                 except:
#                     print('something wrong "login_button.click()"')
#                     message = 'Элемент подсказки не найден'
#             assert message == 'Неверное имя пользователя или пароль.'
#             user.send_keys(Keys.CONTROL + "a")
#             user.send_keys(Keys.DELETE)
#             password.send_keys(Keys.CONTROL + "a")
#             password.send_keys(Keys.DELETE)
#         page.driver.close()
#
#     @allure.story('Авторизация по логину с валидными данными')
#     @allure.severity('Blocker')
#     def test_auth_with_login(self, fox_driver_will_close):
#         """Авторизация по логину"""
#         page = AuthPage(fox_driver_will_close)
#         with allure.step('Заполнение поля "Логин"'):
#             page.get_input_login().send_keys('admin')
#         with allure.step('Заполнение поля "Пароль"'):
#             page.get_input_password().send_keys('testtest1')
#         with allure.step('Нажать на кнопку войти'):
#             page.get_button_login().click()
#             obj = page.driver.find_element(By.CSS_SELECTOR, '.header-contact-us-text__abfM1')
#             assert obj.is_displayed()
#         page.driver.close()
#
#     @allure.story('Авторизация по телефону с валидными данными')
#     @allure.severity('Blocker')
#     def test_auth_with_phone(self, fox_driver_will_close):
#         """Авторизация по телефону"""
#         page = AuthPage(fox_driver_will_close)
#         with allure.step('Заполнение поля "Логин"'):
#             page.get_input_login().send_keys('375336388537')
#         with allure.step('Заполнение поля "Пароль"'):
#             page.get_input_password().send_keys('testtest1')
#         with allure.step('Нажать на кнопку войти'):
#             page.get_button_login().click()
#             obj = page.driver.find_element(By.CSS_SELECTOR, '.header-contact-us-text__abfM1')
#             assert obj.is_displayed()
#         page.driver.close()
#
#     @allure.story('Авторизация по почте с валидными данными')
#     @allure.severity('Blocker')
#     def test_auth_with_email(self, fox_driver_will_close):
#         """Авторизация по почте"""
#         page = AuthPage(fox_driver_will_close)
#         with allure.step('Заполнение поля "Логин"'):
#             page.get_input_login().send_keys('vouka8@yandex.by')
#         with allure.step('Заполнение поля "Пароль"'):
#             page.get_input_password().send_keys('testtest1')
#         with allure.step('Нажать на кнопку войти'):
#             page.get_button_login().click()
#             obj = page.driver.find_element(By.CSS_SELECTOR, '.header-contact-us-text__abfM1')
#             assert obj.is_displayed()
#         page.driver.close()
#
#     @allure.feature('Восстановление пароля')
#     @allure.story('Восстановление пароля по логину')
#     @allure.severity('Critical')
#     def test_recover_password_with_login(self, fox_driver_will_close):
#         """Восстановление пароля по логину"""
#         page = AuthPage(fox_driver_will_close)
#         with allure.step('Наличие линка "Забыли пароль?" и его нажатие'):
#             page.get_recover_password_link().click()
#         with allure.step('Наличие инпута восстановления по логину и ввод в него данных'):
#             page.get_input_restore_password().send_keys('admin')
#         with allure.step('Наличие кнопки "Отправить" и ее нажатие'):
#             page.get_button_send_code().click()
#         with allure.step('Наличие инпута для подтверждения кода'):
#             input_key = page.get_input_send_key()
#         with allure.step('Получение кода из почты и его ввод в инпут подтверждения'):
#             key = get_key()
#             input_key.send_keys(key)
#         with allure.step('Потдверждение авторизации после отправки кода'):
#             send_new_password_button = page.get_button_send_new_password()
#         with allure.step('Прнименение сгенерированного пароля'):
#             send_new_password_button.click()
#         page.driver.close()
#
#     @allure.feature('Восстановление пароля')
#     @allure.story('Авторизация с новым паролем, и установка стандартного пароля')
#     @allure.severity('Critical')
#     def test_auth_with_new_login(self, fox_driver_will_close):
#         """Авторизация с новым паролем, и установка стандартного пароля"""
#         page = AuthPage(fox_driver_will_close)
#         with allure.step('Заполнение поля "Логин"'):
#             page.get_input_login().send_keys('admin')
#         with allure.step('Заполнение поля "Пароль"'):
#             password_get = get_new_password()
#             page.get_input_password().send_keys(password_get)
#         with allure.step('Нажать на кнопку войти'):
#             page.get_button_login().click()
#             obj = page.driver.find_element(By.CSS_SELECTOR, '.header-contact-us-text__abfM1')
#             assert obj.is_displayed()
#         url = 'https://strojregionfilomena.workhere.ru/api/auth/login?_suppress_response_codes=1&expand=partner.partnerHhConfig'
#         data = {"user": "admin", "password": password_get}
#         response = requests.post(url, data=data).json()
#         access = response['data']['token']
#         url_change_password = f'https://api.macroncrm.ru/user/update?id=2&expand=imageLink%2CimageThumbnailLink%2CassignedRights%2Crequisite%2CsignatureObject%2CpassportObjects%2CisWorkObserver%2CimageCropThumbnailLink%2CisGeneralObserver&access-token={access}'
#         with allure.step('Установка нового пароля и его отправка на почту'):
#             requests.post(url_change_password, data={"macron_web_pass": "testtest1"}).json()
#             assert get_new_password() == 'testtest1'
#         page.driver.close()

