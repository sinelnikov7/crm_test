from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_elements(driver, element):
    is_valid = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            element))
    return is_valid