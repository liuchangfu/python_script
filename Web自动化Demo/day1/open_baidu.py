# _*_ coding:utf-8 _*_
# 第一步：导入webdriver模块
import time
from selenium import webdriver
# 第二步：打开火狐浏览器，
driver = webdriver.Chrome()
# 第三步：打开百度
driver.get("https://www.baidu.com")
# 休眠3秒
time.sleep(1)
driver.get("https://www.qq.com")
time.sleep(1)
# # 刷新浏览器
# driver.refresh()
# 后退
driver.back()
time.sleep(1)
# 前进
driver.forward()
# 设置浏览器宽度和高度
driver.set_window_size(800,600)
time.sleep(1)
# 浏览全屏
driver.maximize_window()