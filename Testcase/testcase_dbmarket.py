import time
import unittest
from loguru import logger
from logs.logger import Log
from appium import webdriver
from page.dbmarket import homepage, mytab
from selenium.webdriver.common.by import By
from APP.DB_market import DBmarket_caps
from PublicFunction.Public_board import remotecontrol



class Test_dbmarket(unittest.TestCase):

    def setUp(self) -> None:
        logger.info('-----------测试开始了----------')
        self.driver = webdriver.Remote('http://192.168.18.69:4723/wd/hub', DBmarket_caps)

    def tearDown(self) -> None:
        logger.info('--------------测试结束了----------------')


    # 检查当贝市场我的tab 热播影视点击可以进入资源详情页面；
    def test_01(self):
        driver = self.driver
        time.sleep(5)
        driver.find_element(By.XPATH, homepage.mytab).click()
        time.sleep(3)
        # 点击影视热播
        driver.find_element(By.XPATH, mytab.hotav).click()
        time.sleep(1)
        gethotav_page_resources_1list = driver.find_element(By.XPATH, mytab.hotav_page_resources_1list)
        # 判断是否进入了资源详情页面
        if gethotav_page_resources_1list:
            logger.info('点击我的tab热播影视成功进入资源详情页面')
        else:
            logger.info('error：点击热播影视没有进入资源详情页面')

    # 检查我的tab页面热播影视模块和专题榜单模块展示正常
    def test_02(self):
        driver = self.driver
        time.sleep(2)
        # 进入我的tab页面
        driver.find_element(By.XPATH, homepage.mytab).click()
        time.sleep(2)
        gethotav = driver.find_element(By.XPATH, mytab.hotav)
        time.sleep(2)
        getprojectlist  = driver.find_element(By.XPATH, mytab.projectlist)
        if gethotav and getprojectlist:
            logger.info('我的tab页面热播影视模块和专题榜单模块展示正常')
        else:
            logger.info('error：我的tab页面热播影视模块和专题榜单模块展示异常')

    # 检查我的tab页面，存在已安装应用
    def test_03(self):
        driver = self.driver
        time.sleep(2)
        # 进入我的tab页面
        driver.find_element(By.XPATH, homepage.mytab).click()
        time.sleep(2)
        gethavaapp = driver.find_element(By.XPATH, mytab.havaapp)
        if gethavaapp:
            logger.info('我的tab页面，已安装应用显示正确')
        else:
            logger.info('error:我的tab页面，没有存在已安装的')

    # 检查我的tab页面，已安装的应用可以正常启动使用
    def test_04(self):
        driver = self.driver
        time.sleep(3)
        # 进入我的tab页面
        driver.find_element(By.XPATH, homepage.mytab).click()
        time.sleep(3)
        driver.find_element(By.XPATH, mytab.havaapp).click()
        time.sleep(3)
        gethavaapp_openpage = driver.find_element(By.XPATH, mytab.havaapp_openpage)
        if gethavaapp_openpage:
            logger.info('我的tab页面，已安装的应用可以正常启动使用')
        else:
            logger.info('error:我的tab页面，已安装的应用启动异常')

    # 检查热播影视模块资源页面：本周电影热播、本周电视剧热播、本周综艺热播、本周动漫热播模块展示正确
    def test_05(self):
        driver = self.driver
        time.sleep(2)
        # 进入我的tab页面 打开热播影视
        driver.find_element(By.XPATH, homepage.mytab).click()
        time.sleep(2)
        gethotav = driver.find_element(By.XPATH, mytab.hotav).click()
        time.sleep(3)
        gethotav_page_resources_1list = driver.find_element(By.XPATH, mytab.hotav_page_resources_1list)
        time.sleep(3)
        gethotav_page_resources_2list = driver.find_element(By.XPATH, mytab.hotav_page_resources_2list)
        time.sleep(3)
        gethotav_page_resources_3list = driver.find_element(By.XPATH, mytab.hotav_page_resources_3list)
        time.sleep(3)
        remotecontrol(send='right')
        time.sleep(3)
        remotecontrol(send='right')
        time.sleep(3)
        remotecontrol(send='right')
        time.sleep(3)
        remotecontrol(send='right')
        gethotav_page_resources_4list = driver.find_element(By.XPATH, mytab.hotav_page_resources_4list)
        if gethotav_page_resources_1list and gethotav_page_resources_2list and gethotav_page_resources_3list and gethotav_page_resources_4list:
            logger.info('热播影视模块资源页面：本周电影热播、本周电视剧热播、本周综艺热播、本周动漫热播模块展示正确')
        else:
            logger.info('error: 热播影视模块资源页面，资源列表展示异常请检查')



