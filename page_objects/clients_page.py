from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.by import By


class ClientsPage:

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver
        self.button_create_client = '.plusBlock__AoWbv'
        self.input_client_name = 'CreateLeadForm_ex_name'
        self.button_save_client = '.styles-action-buttons-flex-container__QjsZd.styles-action-buttons-confirm__6Dp1D'

    def get_button_create_client(self):
        create_client_button = self.driver.find_element(By.CSS_SELECTOR, self.button_create_client)
        return create_client_button

    def get_input_client_name(self):
        client_name_input = self.driver.find_element(By.ID, self.input_client_name)
        return client_name_input

    def get_button_save_client(self):
        save_client_button = self.driver.find_element(By.CSS_SELECTOR, self.button_save_client)
        return save_client_button