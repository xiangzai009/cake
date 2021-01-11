from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from test_cake.test_ini import *
def add_goods(driver):
    #进入儿童系列
    driver.find_element_by_class_name('dropdown-toggle').click()
    chilren_page=driver.find_element_by_xpath(config['add']['chilend_item']).click()
    #加入购物车
    try:
        add_goods=driver.find_element_by_css_selector('.item_add.items')
    except NoSuchElementException as error:
        print(error)
        driver.get_screenshot_as_file('../../error/error.png')
    add_goods.click()
    driver.implicitly_wait(3)