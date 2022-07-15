# 当贝市场包信息

DBmarket_caps = {

    # 被测设备和设备Android版本
    'platformName': 'Android',
    'platformVersion': '',

    # 被测设备名
    'deviceName': '当贝市场',

    # 被测产品包名 和 页面
    'appPackage': 'com.dangbeimarket',
    'appActivity': '.activity.WelcomeActivity',

    # 使用自带输入法，输入中文时填True 和 执行完程序恢复原来输入法
    'unicodeKeyboard': True,
    'resetKeyboard': True,

    # 不要重置App 超时 引用库配置信息
    'noReset': True,
    'newCommandTimeout': 60000,
    'automationName': 'UiAutomator2',
    'unlockType': '',
    'unlockKey': ''

}