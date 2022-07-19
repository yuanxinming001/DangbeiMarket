import time
import unittest
from loguru import logger
from appium import webdriver
from page.akeydiagnostic import logget
from page.akeydiagnostic import Network
from page.akeydiagnostic import Network_details
from selenium.webdriver.common.by import By
from APPinfo.Akey_diagnostic import akey_diagnostic_caps



class Test_akeydiagonstic(unittest.TestCase):

    def setUp(self) -> None:
        logger.info('-----------测试开始啦----------')
        self.driver = webdriver.Remote('http://192.168.18.95:4723/wd/hub', akey_diagnostic_caps)

    def tearDown(self) -> None:
        logger.info('--------------测试结束啦----------------')


    # 检查打开一键诊断app，二维码和title显示正确
    def test_01(self):
        driver = self.driver
        time.sleep(5)
        get_Network_inthe_diagnosis_of_button = driver.find_element(By, Network.Network_inthe_diagnosis_of_button)
        time.sleep(10)
        get_Network_inthe_diagnosis_of_title = driver.find_element(By, Network.Network_inthe_diagnosis_of_title)
        if get_Network_inthe_diagnosis_of_button and get_Network_inthe_diagnosis_of_title:
            logger.info('打开一键诊断app，二维码和title显示正确')
        else:
            logger.info('error：打开一键诊断app，二维码和title显示异常，请查看')

    # 检查打开一键诊断app，网络诊断button 和 日志收集button 展示正确
    def test_02(self):
        driver = self.driver
        time.sleep(5)
        get01_Network_inthe_diagnosis_of_button = driver.find_element(By, Network.Network_inthe_diagnosis_of_button)
        time.sleep(2)
        get_logget_start_button = driver.find_element(By, logget.logget_start_button)
        if get01_Network_inthe_diagnosis_of_button and get_logget_start_button:
            logger.info('打开一键诊断app，网络诊断button 和 日志收集button 展示正确')
        else:
            logger.info('error：打开一键诊断app，没有发现网络诊断button 和 日志收集button ')

    # 检查点击一键诊断button 跳转页面正确
    def test_03(self):
        driver = self.driver
        time.sleep(5)
        # click Network_inthe_diagnosis_of_button
        driver.find_element(By, Network.Network_inthe_diagnosis_of_button).click()
        time.sleep(60)
        get_Network_Service_one = driver.find_element(By, Network_details.Network_Service_one)
        get_back = driver.find_element(By, Network_details.back)
        if get_back and get_Network_Service_one:
            logger.info('点击一键诊断button 跳转页面正确')
        else:
            logger.info('error: 点击一键诊断button 跳转页面异常')

    # 检查点击日志收集button 跳转页面正确








