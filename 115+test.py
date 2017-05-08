import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'cfd5ac8a'
        desired_caps['appPackage'] = 'com.yyw.cloudoffice'
        desired_caps['appActivity'] = '.UI.user.account.activity.SplashActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
