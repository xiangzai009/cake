from selenium import webdriver
import xlrd
from test_cake.test_ini import *
def get_value():
    workExcel=xlrd.open_workbook(config.get('file','login_url'),formatting_info=True)
    sheets=workExcel.sheet_names()
    workSheet=workExcel.sheet_by_name('Sheet1')
    url=workSheet.cell(1,0).value
    username=workSheet.cell(1,1).value
    passwod=workSheet.cell(1,2).value
    return url,username,passwod
def login(driver):
    a=list(get_value())
    cake_url = driver.get("http://192.168.1.8:8080"+a[0])
    # 登录按钮
    login_button = driver.find_element_by_xpath(config['login']['submit']).click()
    # 隐式等待
    driver.implicitly_wait(3)
    # 登陆
    usename = driver.find_element_by_name('user.username').send_keys(a[1])
    password = driver.find_element_by_name('user.password').send_keys(a[2])
    # print(usename.get_attribute('placeholder'))
    submit = driver.find_element_by_css_selector(".register-but.text-center").click()
    title=driver.title
    assert '首页1',title
    print('assert is not equal!')