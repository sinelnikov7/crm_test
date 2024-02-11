from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.by import By


class AuthPage:

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver
        self.input_login = 'auth-form-login_user'
        self.input_password = 'auth-form-login_password'
        self.login_button = '.ant-btn-block'
        self.recover_password_link = '.auth-forms-content-fields__tMdk9 > span'
        self.input_restore_password = 'auth-form-restore-password_login'
        self.button_send_code = '.ant-btn.ant-btn-primary'
        self.send_key_input = 'auth-form-restore-password_code'
        self.input_new_password = 'inputPasswordId'
        self.button_send_new_password = "//span[text()='Сохранить']"

    def get_input_login(self):
        input_login = self.driver.find_element(By.ID, self.input_login)
        return input_login

    def get_input_password(self):
        input_password = self.driver.find_element(By.ID, self.input_password)
        return input_password

    def get_button_login(self):
        button_login = self.driver.find_element(By.CSS_SELECTOR, self.login_button)
        return button_login

    def get_recover_password_link(self):
        link_recover_password = self.driver.find_element(By.CSS_SELECTOR, self.recover_password_link)
        return link_recover_password

    def get_input_restore_password(self):
        input_restore_password = self.driver.find_element(By.ID, self.input_restore_password)
        return input_restore_password

    def get_button_send_code(self):
        button_send_code = self.driver.find_element(By.CSS_SELECTOR, self.button_send_code)
        return button_send_code

    def get_input_send_key(self):
        input_send_key = self.driver.find_element(By.ID, self.send_key_input)
        return input_send_key

    def get_input_new_password(self):
        new_password_input = self.driver.find_element(By.ID, self.input_new_password)
        return new_password_input

    def get_button_send_new_password(self):
        send_new_password_button = self.driver.find_element(By.XPATH, self.button_send_new_password)
        return send_new_password_button