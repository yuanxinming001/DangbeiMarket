import uiautomator2
import unittest, time
from appium import webdriver
from selenium.webdriver.common.by import By
from APP.DBmarket_infomation import dbmarket_caps
from PublicFunction.Public_board import remotecontrol
from PublicFunction.Start_app import star_dbmarketapp
from PublicFunction.Public_parameters import ip, apkname
from logs.logger import Log

# 报告存放地址
case_result = '/Users/yuanxinming/Desktop/baogao.html'

# case 条数
casenumber = 0


class ctrip_travel(unittest.TestCase):

    def setUp(self) -> None:
        print('开始执行用例--------------------------------------------------')
        self.driver = webdriver.Remote('http://192.168.18.231:4723/wd/hub', dbmarket_caps)
        # 设置缺省等待时间
        self.driver.implicitly_wait(10)
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert = True  # 是否继续接受下一个警告#

    # 用例1：检查当贝市场可以正常打开app，进入当贝市场首页，检查首页展示正确；
    def test01(self, uiauto2=uiautomator2):
        driver = self.driver
        global casenumber
        casenumber += 1



    # test02：检查我的tab页面热播影视模块和专题榜单模块展示正常
    def test02(self, uiauto2=uiautomator2):
        driver = self.driver
        global casenumber
        rz = Log()
        casenumber += 1
        # 切换到我的tab页面
        time.sleep(2)
        remotecontrol(send='left')
        time.sleep(5)
        remotecontrol(send='left')

        # 点击热播影视进入详情页面
        Popularfilmandtelevision = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[1]'
                                                                 '/android.widget.ImageView').click()

        weekmove = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout'
                                                 '/android.widget.TextView[1]')

        remotecontrol(send='back')

        # 点击专题榜单进入详情页面

        clickztbang = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[2]'
                                                    '/android.widget.ImageView').click()

        zttitle = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                '/android.widget.TextView')

        rz.info('判断是否成功进入热播影视详情页和专题榜单')





