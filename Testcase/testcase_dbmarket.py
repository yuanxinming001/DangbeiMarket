import time
import unittest
from loguru import logger
from logs.logger import Log
from appium import webdriver
from page.dbmarket import home_page, my_tab
from selenium.webdriver.common.by import By
from APPinfo.DB_market import DBmarket_caps
from PublicFunction.Public_board import remotecontrol


class Test_dbmarket(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://192.168.18.95:4723/wd/hub', DBmarket_caps)

    @classmethod
    def tearDownClass(cls):
        logger.info('测试结束')

    # 检查当贝市场我的tab 热播影视点击可以进入资源详情页面；
    def test_01(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, home_page.mytab).click()
        driver.implicitly_wait(3)
        # 点击影视热播
        driver.find_element(By.XPATH, my_tab.hotav).click()
        driver.implicitly_wait(3)
        gethotav_page_resources_1list = driver.find_element(By.XPATH, my_tab.hotav_page_resources_1list)
        # 判断是否进入了资源详情页面
        if gethotav_page_resources_1list:
            logger.info('点击我的tab热播影视成功进入资源详情页面')
        else:
            logger.info('error：点击热播影视没有进入资源详情页面')

    # 检查我的tab页面热播影视模块和专题榜单模块展示正常
    def test_02(self):
        driver = self.driver
        driver.implicitly_wait(3)
        # 进入我的tab页面
        driver.find_element(By.XPATH, home_page.mytab).click()
        driver.implicitly_wait(3)
        gethotav = driver.find_element(By.XPATH, my_tab.hotav)
        driver.implicitly_wait(3)
        getprojectlist  = driver.find_element(By.XPATH, my_tab.projectlist)
        if gethotav and getprojectlist:
            logger.info('我的tab页面热播影视模块和专题榜单模块展示正常')
        else:
            logger.info('error：我的tab页面热播影视模块和专题榜单模块展示异常')

    # 检查我的tab页面，存在已安装应用
    def test_03(self):
        driver = self.driver
        driver.implicitly_wait(3)
        # 进入我的tab页面
        driver.find_element(By.XPATH, home_page.mytab).click()
        driver.implicitly_wait(3)
        gethavaapp = driver.find_element(By.XPATH, my_tab.havaapp)
        if gethavaapp:
            logger.info('我的tab页面，已安装应用显示正确')
        else:
            logger.info('error:我的tab页面，没有存在已安装的')


    # 检查热播影视模块资源页面：本周电影热播、本周电视剧热播、本周综艺热播、本周动漫热播模块展示正确
    def test_04(self):
        driver = self.driver
        driver.implicitly_wait(3)
        # 进入我的tab页面 打开热播影视
        driver.find_element(By.XPATH, home_page.mytab).click()
        driver.implicitly_wait(3)
        gethotav = driver.find_element(By.XPATH, my_tab.hotav).click()
        driver.implicitly_wait(3)
        gethotav_page_resources_1list = driver.find_element(By.XPATH, my_tab.hotav_page_resources_1list)
        driver.implicitly_wait(3)
        gethotav_page_resources_2list = driver.find_element(By.XPATH, my_tab.hotav_page_resources_2list)
        driver.implicitly_wait(3)
        gethotav_page_resources_3list = driver.find_element(By.XPATH, my_tab.hotav_page_resources_3list)
        driver.implicitly_wait(3)
        remotecontrol(send='right')
        driver.implicitly_wait(3)
        remotecontrol(send='right')
        driver.implicitly_wait(3)
        remotecontrol(send='right')
        driver.implicitly_wait(3)
        remotecontrol(send='right')
        gethotav_page_resources_4list = driver.find_element(By.XPATH, my_tab.hotav_page_resources_4list)
        if gethotav_page_resources_1list and gethotav_page_resources_2list and gethotav_page_resources_3list and gethotav_page_resources_4list:
            logger.info('热播影视模块资源页面：本周电影热播、本周电视剧热播、本周综艺热播、本周动漫热播模块展示正确')
        else:
            logger.info('error: 热播影视模块资源页面，资源列表展示异常请检查')



