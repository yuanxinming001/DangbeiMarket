import unittest

if __name__ == '__main__':
    """
    testsuite = unittest.TestLoader().discover('.')通过unittest的TestLoader提供的discover方法去寻找目录中符合条件的测试用例。
    .代表当前目录，也可以构造、传递其他目录。
    以test开头的测试文件名为符合条件的测试用例。
    
    """
    testsuite = unittest.TestLoader().discover('../Testcase')
    unittest.TextTestRunner(verbosity=2).run(testsuite)

