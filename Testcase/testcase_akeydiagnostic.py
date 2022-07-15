import time
import unittest
from loguru import logger
from appium import webdriver
from page.dbmarket import homepage, mytab
from selenium.webdriver.common.by import By
from APP.Akey_diagnostic import akey_diagnostic_caps
from PublicFunction.Public_board import remotecontrol



class Test_akeydiagonstic(unittest.TestCase):

    def setUp(self) -> None:
        logger.info('-----------测试开始啦----------')
        self.driver = webdriver.Remote('http://192.168.18.69:4723/wd/hub', akey_diagnostic_caps)

    def tearDown(self) -> None:
        logger.info('--------------测试结束啦----------------')


    # 检查当贝市场我的tab 热播影视点击可以进入资源详情页面；
    def test_01(self):
        driver = self.driver
        time.sleep(5)
        logger.info('这个app也可以喽')
        remotecontrol(send='ok')
