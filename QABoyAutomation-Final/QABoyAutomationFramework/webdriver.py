from selenium import webdriver


class Driver:

    def __init__(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '64.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768'
        }

        self.instance = webdriver.Remote(
            command_executor='http://mikearias2:6FB489KGkKpshxcFyqzR@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")
