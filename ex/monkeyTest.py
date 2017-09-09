import os
import sys
import time


    
    #
            
    #monkey命令，packageName包名，interval间隔时间单位ms ，frequency执行次数
def monkeyApp(packageName,interval,frequency):
    os.popen("adb shell monkey -p %s --throttle %s --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v %s >\monkeylog\monkeyScreenLog.log" % (packageName, interval, frequency),'r')
        

   
                      
           

    
    

    
packageName = 'com.yyw.cloudoffice'  
monkeyApp(packageName,500,100)
    #判断是否执行完成，执行完成后导出日志
  