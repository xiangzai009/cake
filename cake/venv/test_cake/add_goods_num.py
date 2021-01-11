from selenium import webdriver
from test_cake.login import *
from test_cake.execute_db import *
import MySQLdb
def houtai_login(driver):
    user1 = driver.find_element_by_name('admin.username').clear()
    driver.find_element_by_name('admin.username').send_keys('admin')
    passwd1 = driver.find_element_by_name('admin.password').clear()
    driver.find_element_by_name('admin.password').send_keys('admin')
    login1 = driver.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-block').click()
def add_goods_num(driver):
    goods_mag=driver.find_element_by_link_text('商品管理').click()
    search=driver.find_element_by_name('name').send_keys('小熊乐园')
    submit_search=driver.find_element_by_link_text('点击搜索').click()
    modify=driver.find_element_by_css_selector('.btn.btn-success').click()
    nums=driver.find_element_by_name('good.stock').clear()
    driver.find_element_by_name('good.stock').send_keys('10')
    submit_modify=driver.find_element_by_css_selector('.btn.btn-success').click()
def select_goods_nums(driver):
    rest=execute("select a.stock from goods a where a.name='小熊乐园';")
    if rest[0]<3:
        driver.find_element_by_link_text("后台管理").click()
        #print(driver.current_window_handle)
        #print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[1])
        #print(driver.current_window_handle)
        houtai_login(driver)
        add_goods_num(driver)
        driver.close()
        #print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[0])

