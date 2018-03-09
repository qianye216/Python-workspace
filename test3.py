import uiautomator2 as u2
from time import sleep

d = u2.connect('10.0.6.15')

# 启动App
d.app_start("com.yyw.cloudoffice")

# 搜索
d(resourceId="com.yyw.cloudoffice:id/iv_task_search").click()

# 输入关键字
d(resourceId="com.yyw.cloudoffice:id/search_src_text").set_text("测试")



sleep(2)

# 停止app
d.app_stop("com.yyw.cloudoffice") 