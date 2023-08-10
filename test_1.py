import time
import imaplib
import email

import requests
import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from mail import get_key

def get_key():
    """Получение кода подтверждения при восстановлении пароля из почты"""
    trying = 0
    while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login('vouka8@yandex.by', 'xmlfafkxvimeijkx')
        mail.list()
        mail.select('inbox')
        result, data = mail.search(None, 'UNSEEN')
        ids = data[0]
        if len(ids) > 0:
            id_list = ids.split()
            latest_email_id = id_list[-1]
            result, data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            message = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
            key = message[-6:]
            print(email_message['Date'])
            return key
        else:
            time.sleep(1)
            trying += 1
            if  trying > 10:
                return 'Письмо не пришло'

def get_new_password():
    """Получение нового пароля из почты"""
    trying = 0
    while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login('vouka8@yandex.by', 'xmlfafkxvimeijkx')
        mail.list()
        mail.select('inbox')
        result, data = mail.search(None, 'UNSEEN')
        ids = data[0]
        if len(ids) > 0:
            id_list = ids.split()
            latest_email_id = id_list[-1]
            result, data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            message = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
            splited = message.split('Пароль: ')[1]
            password = splited[0:9]
            return password
        else:
            time.sleep(1)
            trying += 1
            if  trying > 10:
                return 'Письмо не пришло'

# def test_auth_with_invalid_data(chrome_driver_will_close, fox_driver_will_close):
# def test_auth_with_invalid_data(fox_driver_will_close):
#     """Авторизация с невалидными данными"""
#     # browsers = [chrome_driver_will_close, fox_driver_will_close]
#     browsers = [fox_driver_will_close]
#     data = [
#         {'login': 'admins', 'password': 'testtest1'},
#         {'login': 'admin', 'password': 'testtest'},
#         {'login': 'admins', 'password': 'testtest'}
#     ]
#     for browser in browsers:
#         browser.implicitly_wait(5)
#         browser.get('https://strojregionfilomena.workhere.ru/')
#         user = browser.find_element(By.ID, "auth-form-login_user")
#         password = browser.find_element(By.ID, 'auth-form-login_password')
#         login_button = browser.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#         for value in data:
#             user.send_keys(value.get('login'))
#             password.send_keys(value.get('password'))
#             try:
#                 WebDriverWait(browser, 5).until(EC.element_to_be_clickable(login_button))
#                 login_button.click()
#             except:
#                 print('something wrong "login_button.click()"')
#             message = browser.find_element(By.CSS_SELECTOR, '.auth-forms-content-fields-message__hIBT7')
#             assert message.text == 'Неверное имя пользователя или пароль.'
#             user.send_keys(Keys.CONTROL + "a")
#             user.send_keys(Keys.DELETE)
#             password.send_keys(Keys.CONTROL + "a")
#             password.send_keys(Keys.DELETE)
#     # chrome_driver_will_close.close()
#     fox_driver_will_close.close()
#
# def test_auth_with_login(fox_driver_will_close):
#     """Авторизация по логину"""
#     browsers = [fox_driver_will_close]
#     for browser in browsers:
#         browser.implicitly_wait(5)
#         browser.get('https://strojregionfilomena.workhere.ru/')
#         user = browser.find_element(By.ID, "auth-form-login_user")
#         password = browser.find_element(By.ID, 'auth-form-login_password')
#         login_button = browser.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#         user.send_keys('admin')
#         password.send_keys('testtest1')
#         login_button.click()
#         time.sleep(2)
#         message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div')
#         assert message.text == 'Вы успешно вошли'
#         browser.close()
#
# def test_auth_with_phone(fox_driver_will_close):
#     """Авторизация по номеру телефона"""
#     browsers = [fox_driver_will_close]
#     for browser in browsers:
#         browser.implicitly_wait(5)
#         browser.get('https://strojregionfilomena.workhere.ru/')
#         user = browser.find_element(By.ID, "auth-form-login_user")
#         password = browser.find_element(By.ID, 'auth-form-login_password')
#         login_button = browser.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#         user.send_keys('74956468444')
#         password.send_keys('testtest1')
#         login_button.click()
#         time.sleep(2)
#         message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div')
#         assert message.text == 'Вы успешно вошли'
#         browser.close()
#
# def test_auth_with_email(fox_driver_will_close):
#     """Авторизация по email"""
#     browsers = [fox_driver_will_close]
#     for browser in browsers:
#         browser.implicitly_wait(5)
#         browser.get('https://strojregionfilomena.workhere.ru/')
#         user = browser.find_element(By.ID, "auth-form-login_user")
#         password = browser.find_element(By.ID, 'auth-form-login_password')
#         login_button = browser.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#         user.send_keys('vouka8@yandex.by')
#         password.send_keys('testtest1')
#         login_button.click()
#         time.sleep(2)
#         message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div')
#         assert message.text == 'Вы успешно вошли'
#         browser.close()
#
#
# def test_recover_password_with_login(fox_driver_will_close):
#     """Восстановление пароля по логину"""
#     browser = fox_driver_will_close
#     browser.implicitly_wait(20)
#     browser.get('https://strojregionfilomena.workhere.ru/')
#     link = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/section/section/section/main/div/div/form/div[1]/span')
#     link.click()
#     input_login = browser.find_element(By.XPATH, '//*[@id="auth-form-restore-password_login"]')
#     input_login.send_keys('admin')
#     button = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/section/section/section/main/div/div/form/div[1]/div[2]/div/div/span/button')
#     button.click()
#     input_key = browser.find_element(By.XPATH, '//*[@id="auth-form-restore-password_code"]')
#     key = get_key()
#     input_key.send_keys(key)
#     button = browser.find_element(By.XPATH, '/html/body/div/div/div/section/section/section/main/div/div/form/div[1]/div[2]/div/div/span/button')
#     button.click()
#     time.sleep(5)
#     try:
#         is_valid = WebDriverWait(browser, 20).until(
#                     EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/div')))
#     except Exception:
#         browser.close()
#     assert is_valid.is_displayed()
#     button_aprove = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/button[1]')
#     button_aprove.click()
#     browser.close()
#
#
# def test_auth_with_new_login(fox_driver_will_close):
#     """Авторизация с новым паролем, и установка стандартного пароля"""
#     browser = fox_driver_will_close
#     browser.implicitly_wait(5)
#     browser.get('https://strojregionfilomena.workhere.ru/')
#     user = browser.find_element(By.ID, "auth-form-login_user")
#     password = browser.find_element(By.ID, 'auth-form-login_password')
#     login_button = browser.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#     user.send_keys('admin')
#     password_get = get_new_password()
#     password.send_keys(password_get)
#     login_button.click()
#     time.sleep(2)
#     message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div')
#     assert message.text == 'Вы успешно вошли'
#     url = 'https://strojregionfilomena.workhere.ru/api/auth/login?_suppress_response_codes=1&expand=partner.partnerHhConfig'
#     data = {"user":"admin", "password": password_get}
#     # data = {"user":"admin", "password": 'testtest1'}
#     response = requests.post(url, data=data).json()
#     access = response['data']['token']
#     url_change_password = f'https://api.macroncrm.ru/user/update?id=2&expand=imageLink%2CimageThumbnailLink%2CassignedRights%2Crequisite%2CsignatureObject%2CpassportObjects%2CisWorkObserver%2CimageCropThumbnailLink%2CisGeneralObserver&access-token={access}'
#     requests.post(url_change_password, data={"macron_web_pass": "testtest1"}).json()
#     assert get_new_password() == 'testtest1'
#     browser.close()

# def test_5(fox_driver_wont_close):
#     fox_driver_wont_close.get('https://strojregionfilomena.workhere.ru/')
#     fox_driver_wont_close.implicitly_wait(10)
#     user = fox_driver_wont_close.find_element(By.ID, "auth-form-login_user")
#     password = fox_driver_wont_close.find_element(By.ID, 'auth-form-login_password')
#     login_button = fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#     user.send_keys('admin')
#     password.send_keys('testtest1')
#     login_button.click()
#     dropdown = fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.user-dropdown__lNpwN')
#     assert dropdown.is_displayed()


# def test_tools(fox_driver_wont_close):
#     fox_driver_wont_close.get('https://strojregionfilomena.workhere.ru/')
#     fox_driver_wont_close.find_element(By.XPATH, '//a[starts-with(@href,"/tools")]').click()
#     assert fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.title__8XLeH').text == 'Инструменты'
#     time.sleep(2)
#     fox_driver_wont_close.find_element(By.XPATH, '//a[starts-with(@href, "/key-management")]').click()
#     assert fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.title__8XLeH').text == 'Управление ключами'
#     # table = fox_driver_wont_close.find_element(By.XPATH, '//tbody[@class="ant-table-tbody"]')
#     # count = table.get_attribute('childElementCount')
#     # count = table.get_attribute('outerHTML')
#     add_key = fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.plusBlock__AoWbv')
#     # add_key = fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.ant-notification-notice')
#     time.sleep(7)
#     # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='taLnk ulBlueLinks']"))).click()
#     # fox_driver_wont_close.execute_script('arguments[0].click;', add_key)
#     add_key.click()
#     fox_driver_wont_close.find_element(By.TAG_NAME, 'input').send_keys('2')
#     fox_driver_wont_close.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-primary"]').click()
#     time.sleep(5)
#     assert fox_driver_wont_close.find_element(By.XPATH,
#                                               '//div[@class="dialog-header-default-title-name__yeBEd"]/div').text == 'Информация о ключе'
#     fox_driver_wont_close.find_element(By.XPATH,
#                                        '//div[@class="keyManagement__dialog__footer__OQ45J"]/button').click()
#     raw = fox_driver_wont_close.find_element(By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[2]')
#     # print(raw.get_attribute('outerHTML'))
#     key = raw.find_element(By.XPATH, '//span[@class="key-field__box__3fUIb"]').text
#     print(key)
#     raw.find_element(By.XPATH, '//button[@class="key-field__control__EDtFi"]').click()
#     time.sleep(10)
#     fox_driver_wont_close.find_element(By.CSS_SELECTOR, '.plusBlock__AoWbv').click()
#     a = fox_driver_wont_close.find_element(By.TAG_NAME, 'input')
#     a.send_keys(Keys.CONTROL + "v")
#     time.sleep(5)
#     validate_key = a.get_attribute('value')
#     assert key == validate_key


# def test_create_clients(fox_driver_wont_close, access_token):
#     """Создание и редактирование клиента"""
#     browser = fox_driver_wont_close
#     wait = WebDriverWait(browser, 10)
#     browser.implicitly_wait(10)
#     browser.get('https://strojregionfilomena.workhere.ru/clients')
#     # create_button = browser.find_element(By.CSS_SELECTOR, '.addButtonWrapper__FmKJO')
#     create_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.addButtonWrapper__FmKJO')))
#     create_button.click()
#     input_client_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="CreateLeadForm_ex_name"]')))
#     input_client_name.send_keys(f'{datetime.date.today()} - 0')
#     button_save_client = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button_save_client.click()
#     statuses = ([6, 2], [4, 4], [3, 5])
#     for status in statuses:
#         print(access_token)
#         data_now = datetime.datetime.now()
#         name = f"{data_now.day}-{data_now.month}-{data_now.year} {data_now.hour}:{data_now.minute}:{data_now.second}"
#         url = f'https://api.macroncrm.ru/express-client/create?disable_black_list_check=1&access-token={access_token}'
#         data = {
#             "client_stts": status[0], "contr_stts": status[1], "ex_name": name, "deal_availability": 0,
#             "name_creator": "Admin", "respon_client_stts": "Admin", "uid_creator": 2
#         }
#         assert requests.post(url, data=data).status_code == 201
    # browser.close()

#NoSuchElementException
def test_check_value_vidget_clients(browser_autorized_mozila):
    """Проверка значений статистики клиентов в виджете и на вкладке"""
    browser = browser_autorized_mozila
    wait = WebDriverWait(browser, 10)
    browser.implicitly_wait(10)
    browser.get('https://strojregionfilomena.workhere.ru/')
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://strojregionfilomena.workhere.ru/clients')
    radio_group = browser.find_element(By.XPATH, '//div[@class="ant-radio-group ant-radio-group-outline"]/label[1]')
    radio_group.click()
    time.sleep(5)
    client_status = browser.find_element(By.XPATH, '//div[@id="rc-tabs-0-tab-1"]')
    client_status.click()
    assert browser.find_element(By.XPATH, '//div[@class="quick-stats__block__2eDvm"]').is_displayed() == True
    index = 1
    status_list = '//div[@class="quick-stats__block__2eDvm"]'
    dict_from_vkladka = {'name': [], 'value': [], 'procent': []}
    while True:
        try:
            dict_from_vkladka['name'].append(browser.find_element(By.XPATH, f'{status_list}/div[{index}]/div/div').text)
            dict_from_vkladka['value'].append(browser.find_element(By.XPATH, f'{status_list}/div[{index}]/span/div').text)
            dict_from_vkladka['procent'].append(browser.find_element(By.XPATH, f'{status_list}/div[{index}]/div[2]/div/span').text)
            index += 1
        except NoSuchElementException:
            print(dict_from_vkladka)
            break









# def test_invalid_password(chrome_driver_wont_close):
#     chrome_driver_wont_close.implicitly_wait(5)
#     chrome_driver_wont_close.get('https://strojregionfilomena.workhere.ru/')
#     try:
#         user = WebDriverWait(chrome_driver_wont_close, 5).until(
#             EC.presence_of_element_located((By.ID, "auth-form-login_user"))
#         )
#     except Exception:
#         chrome_driver_wont_close.close()
#     password = chrome_driver_wont_close.find_element(By.ID, 'auth-form-login_password')
#     login_button = chrome_driver_wont_close.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#     user.send_keys('admin')
#     password.send_keys('testtest2')
#     login_button.click()
#     message = chrome_driver_wont_close.find_element(By.CSS_SELECTOR, '.auth-forms-content-fields-message__hIBT7')
#     assert message.text == 'Неверное имя пользователя или пароль.'
#
#
# def test_valid_login(chrome_driver_wont_close):
#     chrome_driver_wont_close.implicitly_wait(5)
#     chrome_driver_wont_close.get('https://strojregionfilomena.workhere.ru/')
#     user = chrome_driver_wont_close.find_element(By.ID, 'auth-form-login_user')
#     password = chrome_driver_wont_close.find_element(By.ID, 'auth-form-login_password')
#     login_button = chrome_driver_wont_close.find_element(By.CSS_SELECTOR, '.ant-btn-block')
#     user.send_keys('admin')
#     password.send_keys('testtest1')
#     login_button.click()
#     assert "СтройРегион.Филомена" in chrome_driver_wont_close.title
#     try:
#         auth = WebDriverWait(chrome_driver_wont_close, 7).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR,
#                                             '.header-collapse-block-wrapper__p4hkl')))
#     except Exception:
#         chrome_driver_wont_close.close()
#     name = chrome_driver_wont_close.find_element(By.XPATH, '//div[starts-with(@class, "text-overflow__aqy+a")]')
#     # print(name.location)
#     # print(name.rect)
#
#
# def test_valid_1(chrome_driver_wont_close):
#     chrome_driver_wont_close.implicitly_wait(5)
#     chrome_driver_wont_close.get('https://strojregionfilomena.workhere.ru/')
#     button = chrome_driver_wont_close.find_element(By.CSS_SELECTOR, '.header-collapse-block-wrapper__p4hkl')
#     button.click()
#     tools_menu = chrome_driver_wont_close.find_element(By.XPATH, '//a[starts-with(@href,"/tools")]')
#     tools_menu.click()
#     tools_menu.screenshot('tools_menu.png')
#     key_management = chrome_driver_wont_close.find_element(By.XPATH, '//a[starts-with(@href,"/key-management")]')
#     key_management.screenshot('key_management.png')
#     key_management.click()
#     title = chrome_driver_wont_close.find_element(By.CSS_SELECTOR, '.title__8XLeH')
#     assert title.text == 'Управление ключами'
#     time.sleep(5)
#     # row = driver.find_element(By.XPATH, '//tr[starts-with(@class, "ant-table-row")]')
#     # row = driver.find_element(By.XPATH, '//tr[@class=".ant-table-row-level-0"]')
#     # a = driver.find_element(By.XPATH, '//tbody[@class="ant-table-tbody"]/child::*')
#     # a = driver.find_element(By.ID, 'KeyManagement')
#     # print(dir(a))
#     # print(a.__dict__)
#     # print(a.get_attribute('class'))
#     # v = a.find_element(By.XPATH, "*")
#     # for child in v.get_attribute('outerHTML'):
#     #     print("\nChild Element")
#     #     print(child.get_attribute('outerHTML'))
#     # print(v.get_attribute('outerHTML'))
#     # print(row)
#     # print(row.get_attribute('data-row-key'))
#     # print(dir(row))
#     # g = driver.find_element(By.TAG_NAME, 'thead')
#     x = chrome_driver_wont_close.find_element(By.TAG_NAME, 'tbody')
#     # qqq = x.find_element(By.XPATH, '*')
#     # for q in qqq:
#     #     print('!')
#     print(x.get_attribute('outerHTML'))
#     chrome_driver_wont_close.close()
