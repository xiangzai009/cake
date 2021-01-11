import random
def submit_order(driver):
    #进入购物车
    shopping_cart=driver.find_element_by_css_selector('.glyphicon.glyphicon-shopping-cart').click()
    #增加商品数量
    add_num=driver.find_element_by_css_selector('.btn.btn-info').click()
    #提交订单
    order_submit=driver.find_element_by_css_selector('.btn.btn-success.btn-lg').click()
    address = driver.find_element_by_id('faddress').send_keys('上海' + str(random.randrange(99)))
    driver.find_element_by_class_name('thumbnail').click()
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector('.btn.btn-success').click()
    driver.close()