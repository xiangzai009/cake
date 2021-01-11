from selenium import webdriver
from test_cake.login import *
from test_cake.add_goods import *
from test_cake.add_goods_num import *
from test_cake.order import *
from selenium.common.exceptions import NoSuchElementException
from HTMLTestRunner import HTMLTestRunner
from test_cake.log.log import *
import pytest
import unittest
driver = webdriver.Firefox()
#class TestUnit(unittest.TestCase):
def test_order():
    login(driver)
    logger.info('用户登录成功')
    select_goods_nums(driver)
    add_goods(driver)
    logger.info('用户添加商品成功')
    submit_order(driver)
if __name__=='__main__':
    pytest.main(['main.py','-s','--html=../../report/pytestreport.html'])
    '''
    filepath='../../report/htmlreport.html'
    with open(filepath,'wb') as fp:
        f=unittest.TestSuite()
        f.addTest(TestUnit('test_order'))
        runner=HTMLTestRunner(fp,verbosity=2,title='测试报告')
        runner.run(f)
        print('666')
    '''