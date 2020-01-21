from selenium import webdriver


class Store:
    drivers = []
    current_driver = None
    static_data_path = None
    dynamic_data_path = None
    global_data_path = None

    @classmethod
    def push(self, driver: webdriver) -> webdriver:
        self.drivers.append(driver)
        self.set_current_driver(driver)

    @classmethod
    def set_current_driver(self, driver: webdriver) -> webdriver:
        self.current_driver = driver

    @classmethod
    def switch_driver(self, driver) -> webdriver:
        self.current_driver = driver
