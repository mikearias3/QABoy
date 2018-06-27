from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
            'platformName': 'android',
            'deviceName': 'OnePlus 6',
            'appPackage': 'com.oneplus.calculator',
            'appActivity': 'com.oneplus.calculator.Calculator'
        }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
