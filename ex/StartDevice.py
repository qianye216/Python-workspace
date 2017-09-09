# coding=utf-8
import time
from appium import webdriver

class StartDevice():
    def __init__(self):     #初始化
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'b2aada47',
            'platformVersion': '7.0',
            'appPackage': 'com.yyw.cloudoffice',
            'appActivity': 'com.yyw.cloudoffice.UI.user.account.activity.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.desired_caps['noReset'] = True
    def start_driver(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps )
        print("安卓APP自动化Start..."+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return driver

# 9d43fc29   7.0
# a2e8be3c   5.1.1
# localhost   127.0.0.1