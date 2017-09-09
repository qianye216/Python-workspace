# coding=utf-8
import random
import time
from Pythonworkspace.ex.StartDevice import StartDevice

class add_zuzhi():
    def __init__(self):
        Device = StartDevice()
        self.driver = Device.start_driver()
        self.num = random.randint(1000,9999)

    def test_add_quanzi001(self):    #测试用例
        # self.driver.wait_activity('.UI.MainBossActivity',60,1)  #等待页面加载出现
        time.sleep(12)
        self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.RelativeLayout[1]').click()
        print('进入组织')
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView[@resource-id=\"com.yyw.cloudoffice:id/recycler_view\"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]').click()
            print('打开圈子')
            time.sleep(4)
        except BaseException as reason:
            self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\"转到上一层级\"]').click()
            print('返回通知')
            time.sleep(1)

    def test_wofade002(self):
        self.driver.find_element_by_id('com.yyw.cloudoffice:id/ll_name_text').click()        #打开动态详情
        time.sleep(2)
        # self.swipe(100,100,100,100,500)   #更多
        self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout[3]').click() # 点击关联事务
        time.sleep(3)
        self.driver.find_element_by_id('com.yyw.cloudoffice:id/category_choose_layout').click()     #点击事务
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.RelativeLayout[1]').click()    #点击成员




        self.driver.find_element_by_id('com.yyw.cloudoffice:id/tv_task_title').click()   #点击事务
        time.sleep(1)
        self.driver.find_element_by_id('android:id/button1').click()   # 确定



        # self.driver.close_app()
        # self.driver.quit()

memo = add_zuzhi()
memo.test_add_quanzi001()
memo.test_wofade002()