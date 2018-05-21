# _*_ coding:utf-8 _*_
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(1)
# 保存至当前目录，保存图只能为.png格式
driver.get_screenshot_as_file("./baidu.png")
# 保存至根目录，保存图只能为.png格式
driver.get_screenshot_as_file("../baidu.png")
driver.quit()