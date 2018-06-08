# _*_ coding:utf-8 _*_
from selenium import webdriver

options = webdriver.ChromeOptions()
options.set_headless()

options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file('test.png')
driver.close()