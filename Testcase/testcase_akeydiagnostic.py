import time
import unittest
from loguru import logger
from appium import webdriver
from page.akeydiagnostic import logget
from page.akeydiagnostic import Network
from page.akeydiagnostic import Network_details
from selenium.webdriver.common.by import By
from APPinfo.Akey_diagnostic import akey_diagnostic_caps
from PublicFunction.Public_board import remotecontrol



class Test_akeydiagonstic(unittest.TestCase):

    def setUp(self) -> None:
        logger.info('测试开始')
        self.driver = webdriver.Remote('http://192.168.18.95:4723/wd/hub', akey_diagnostic_caps)

    def tearDown(self) -> None:
        logger.info('测试结束')


    # 检查打开一键诊断app，二维码和title显示正确
    def test_01(self):
        driver = self.driver
        driver.implicitly_wait(3)
        get_Network_inthe_diagnosis_of_button = driver.find_element(By.XPATH, Network.Network_inthe_diagnosis_of_button)
        driver.implicitly_wait(10)
        time.sleep(1)
        get_Network_inthe_diagnosis_of_title = driver.find_element(By.XPATH, Network.Network_inthe_diagnosis_of_title)
        if get_Network_inthe_diagnosis_of_button and get_Network_inthe_diagnosis_of_title:
            logger.info('打开一键诊断app，二维码和title显示正确')
        else:
            logger.info('error：打开一键诊断app，二维码和title显示异常，请查看')

    # 检查打开一键诊断app，网络诊断button 和 日志收集button 展示正确
    def test_02(self):
        driver = self.driver
        driver.implicitly_wait(3)
        get01_Network_inthe_diagnosis_of_button = driver.find_element(By.XPATH, Network.Network_inthe_diagnosis_of_button)
        driver.implicitly_wait(3)
        get_logget_start_button = driver.find_element(By.XPATH, logget.logget_start_button)
        if get01_Network_inthe_diagnosis_of_button and get_logget_start_button:
            logger.info('打开一键诊断app，网络诊断button 和 日志收集button 展示正确')
        else:
            logger.info('error：打开一键诊断app，没有发现网络诊断button 和 日志收集button ')

    # 检查点击一键诊断button 跳转页面正确
    def test_03(self):
        driver = self.driver
        driver.implicitly_wait(3)
        # click Network_inthe_diagnosis_of_button
        driver.find_element(By.XPATH, Network.Network_inthe_diagnosis_of_button).click()
        driver.implicitly_wait(25)
        get_Network_Service_one = driver.find_element(By.XPATH, Network_details.Network_Service_one)
        get_back = driver.find_element(By.XPATH, Network_details.back)
        if get_back and get_Network_Service_one:
            logger.info('点击一键诊断button 跳转页面正确')
        else:
            logger.info('error: 点击一键诊断button 跳转页面异常')

    # 检查点击日志收集button 跳转页面正确
    def test_04(self):
        driver = self.driver
        driver.implicitly_wait(3)
        remotecontrol(send='right')
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, logget.logget_button).click()
        driver.implicitly_wait(3)
        get_logget_one = driver.find_element(By.XPATH, logget.logget_one)
        driver.implicitly_wait(3)
        get_logget_two = driver.find_element(By.XPATH, logget.logget_two)
        if get_logget_one and get_logget_two:
            logger.info('点击日志收集button 跳转页面正确')
        else:
            logger.info('error:点击日志收集button 跳转页面错误 请检查')


    # 检查点击日志收集button,可以正常收集日志
    def test_05(self):
        driver = self.driver
        driver.implicitly_wait(5)
        remotecontrol(send='right')
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, logget.logget_button).click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, logget.logget_start_button).click()
        driver.implicitly_wait(5)
        # 获取上报时间icon
        get_log_time_icon = driver.find_element(By.XPATH, logget.get_log_time)
        if get_log_time_icon:
            logger.info('点击日志收集button,可以正常收集日志')
        else:
            logger.info('error:点击日志收集button,无法收集日志，请检查')

    # 检查点击上报日志可以正常上报成功
    def test_06(self):
        driver = self.driver
        driver.implicitly_wait(5)
        remotecontrol(send='right')
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, logget.logget_button).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, logget.logget_start_button).click()
        logger.info('已经开始上报日志了，需要等待30s 有效上报时间')
        driver.implicitly_wait(50)
        driver.find_element(By.XPATH, logget.log_upload).click()
        driver.implicitly_wait(10)
        GET_Network_inthe_diagnosis_of_button = driver.find_element(By.XPATH, Network.Network_inthe_diagnosis_of_button)
        if GET_Network_inthe_diagnosis_of_button:
            logger.info('点击上报日志可以正常上报成功')
        else:
            logger.info('error:点击上报日志,无法成功上报日志，请检查')

    # 检查首页的二维码存在，展示正确
    def test_07(self):
        driver = self.driver
        driver.implicitly_wait(5)
        get_Network_inthe_diagnosis_of_button = driver.find_element(By.XPATH, Network.Network_inthe_diagnosis_of_button)
        driver.implicitly_wait(10)
        get_Qr_code = driver.find_element(By.XPATH, Network.Qr_code)
        if get_Network_inthe_diagnosis_of_button and get_Qr_code:
            logger.info('打开一键诊断app，二维码显示正确')
        else:
            logger.info('error：打开一键诊断app，二维码显示异常，请查看')
















