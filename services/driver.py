from selenium.webdriver import Firefox

class FoxDriver(Firefox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicitly_wait(5)