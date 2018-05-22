# _*_ coding:utf-8 _*_
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
# 鼠标悬停在设置按钮上
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()

