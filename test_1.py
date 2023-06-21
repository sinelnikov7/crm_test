import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login(driver):
    driver.implicitly_wait(5)
    driver.get('https://strojregionfilomena.workhere.ru/')
    try:
        user = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "auth-form-login_user"))
        )
    except Exception:
        driver.close()
    password = driver.find_element(By.ID, 'auth-form-login_password')
    login_button = driver.find_element(By.CSS_SELECTOR, '.ant-btn-block')
    user.send_keys('admins')
    password.send_keys('testtest1')
    login_button.click()
    message = driver.find_element(By.CSS_SELECTOR, '.auth-forms-content-fields-message__hIBT7')
    assert message.text == 'Неверное имя пользователя или пароль.'


def test_invalid_password(driver):
    driver.implicitly_wait(5)
    driver.get('https://strojregionfilomena.workhere.ru/')
    try:
        user = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "auth-form-login_user"))
        )
    except Exception:
        driver.close()
    password = driver.find_element(By.ID, 'auth-form-login_password')
    login_button = driver.find_element(By.CSS_SELECTOR, '.ant-btn-block')
    user.send_keys('admin')
    password.send_keys('testtest2')
    login_button.click()
    message = driver.find_element(By.CSS_SELECTOR, '.auth-forms-content-fields-message__hIBT7')
    assert message.text == 'Неверное имя пользователя или пароль.'


def test_valid_login(driver):
    driver.implicitly_wait(5)
    driver.get('https://strojregionfilomena.workhere.ru/')
    user = driver.find_element(By.ID, 'auth-form-login_user')
    password = driver.find_element(By.ID, 'auth-form-login_password')
    login_button = driver.find_element(By.CSS_SELECTOR, '.ant-btn-block')
    user.send_keys('admin')
    password.send_keys('testtest1')
    login_button.click()
    assert "СтройРегион.Филомена" in driver.title
    try:
        auth = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            '.header-collapse-block-wrapper__p4hkl')))
    except Exception:
        driver.close()
    name = driver.find_element(By.XPATH, '//div[starts-with(@class, "text-overflow__aqy+a")]')
    # print(name.location)
    # print(name.rect)


def test_valid_1(driver):
    driver.implicitly_wait(5)
    driver.get('https://strojregionfilomena.workhere.ru/')
    button = driver.find_element(By.CSS_SELECTOR, '.header-collapse-block-wrapper__p4hkl')
    button.click()
    tools_menu = driver.find_element(By.XPATH, '//a[starts-with(@href,"/tools")]')
    tools_menu.click()
    tools_menu.screenshot('tools_menu.png')
    key_management = driver.find_element(By.XPATH, '//a[starts-with(@href,"/key-management")]')
    key_management.screenshot('key_management.png')
    key_management.click()
    title = driver.find_element(By.CSS_SELECTOR, '.title__8XLeH')
    assert title.text == 'Управление ключами'
    time.sleep(5)
    # row = driver.find_element(By.XPATH, '//tr[starts-with(@class, "ant-table-row")]')
    # row = driver.find_element(By.XPATH, '//tr[@class=".ant-table-row-level-0"]')
    # a = driver.find_element(By.XPATH, '//tbody[@class="ant-table-tbody"]/child::*')
    a = driver.find_element(By.CLASS_NAME, 'ant-table-tbody')
    print(dir(a))
    print(a.__dict__)
    print(a.get_attribute('class'))
    v = a.find_element(By.XPATH, "*")
    print(v.get_attribute('class'))
    # print(row)
    # print(row.get_attribute('data-row-key'))
    # print(dir(row))
    driver.close()
