from logs.logger import Log
from appium import webdriver
from APP.DBmarket_infomation import dbmarket_caps



# 启动当贝市场函数
def star_dbmarketapp():
    rz = Log()
    webdriver.Remote('http://192.168.18.231:4723/wd/hub', dbmarket_caps)
    rz.info('成功打开了当贝市场app')
