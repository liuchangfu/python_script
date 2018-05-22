# _*_ coding:utf-8 _*_
from selenium import webdriver

drvier = webdriver.Chrome()
drvier.get("https://mail.163.com/")
drvier.implicitly_wait(10)
# 定位到iframe
drvier.switch_to.frame("x-URS-iframe")
drvier.find_element_by_name("email").send_keys("18620059772")
drvier.find_element_by_name("password").send_keys("121241111")
drvier.switch_to.default_content()
