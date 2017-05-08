import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    # 脚本初始化,获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'cfd5ac8a'
        desired_caps['appPackage'] = 'com.miui.calculator'
        desired_caps['appActivity'] = '.cal.CalculatorActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    # 释放实例,释放资源
    def tearDown(self):
        self.driver.quit()

    #测试的脚本, LOVE原则
    def testAdd(self):
        # Locate 定位一个元素
        number8 = self.driver.find_element_by_id("btn_8")
        # Operate 操作一个元素
        number8.click()
        # Locate 定位一个元素
        addopertion = self.driver.find_element_by_id("btn_plus")
        # Operate 操作一个元素
        addopertion.click()
        # Locate 定位一个元素
        number5 = self.driver.find_element_by_id("btn_5")
        # Operate 操作一个元素
        number5.click()
        # Locate 定位一个元素
        equal = self.driver.find_element_by_id("等于")
        # Operate 操作一个元素
        equal.click()

        # Verify 验证操作的结果
        result = self.driver.find_element_by_xpath(
            "//*[1]//*[1]//*[2]//*[1]//*[1]//*[1]//*[1]//*[3]//*[1]//*[2]")
        value = result.text
        self.assertEqual(u"13", value)
        # Exception 处理异常的情况


if __name__ == '__main__':
    unittest.main()
