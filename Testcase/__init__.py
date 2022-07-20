import unittest

if __name__ == '__main__':
    """
    ·执行Testcase 下面所有app的case，不会产生报告；
    ·testsuite = unittest.TestLoader().discover('.')通过unittest的TestLoader提供的discover方法去寻找目录中符合条件的测试用例。
    .代表当前目录，也可以构造、传递其他目录。
    ·以test开头的测试文件名为符合条件的测试用例。
    ·产生报告执行请在Terminal中执行pytes
    
    """
    testsuite = unittest.TestLoader().discover('../Testcase')
    unittest.TextTestRunner(verbosity=2).run(testsuite)

