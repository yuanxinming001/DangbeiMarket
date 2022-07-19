from logs.logger import Log
from appium import webdriver
from APPinfo.Projection_housekeeper import Projection_housekeeper_caps



# 启动当贝市场函数
def star_Projection_housekeeper():
    rz = Log()
    webdriver.Remote('http://192.168.18.95:4723/wd/hub', Projection_housekeeper_caps)
    rz.info('成功打开了当贝市场app')


star_Projection_housekeeper()