import configparser
#driver = webdriver.Firefox()
config=configparser.ConfigParser() #类实例化
c=config.read('../common/config.ini')
print(c)
print(config['add']['chilend_item'])