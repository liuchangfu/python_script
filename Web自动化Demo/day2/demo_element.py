# _*_ coding:utf-8 _*_
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("博客园")
driver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='kw']").clear()

driver.find_element_by_xpath("//input[@id='kw']").send_keys("中国移动官网")
driver.find_element_by_xpath("//input[@id='su']").submit()