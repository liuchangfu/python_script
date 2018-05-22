# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.maximize_window()

# 通过xpath中的id属性定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='kw']").clear()

# 通过xpath中的name属性定位
driver.find_element_by_xpath("//input[@name='wd']").send_keys("java")
time.sleep(3)
driver.find_element_by_xpath("//input[@name='wd']").clear()

# 通过xpath中的class属性定位
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("QTP")
time.sleep(3)
driver.find_element_by_xpath("//input[@class='s_ipt']").clear()

# 通过xpath中的其它属性定位
# driver.findElement(By.xpath("//input[contains(@autocomplete,'off')]"))
driver.find_element_by_xpath("//input[contains(@autocomplete,'off')]").send_keys("LR")
time.sleep(3)
driver.find_element_by_xpath("//input[contains(@autocomplete,'off')]").clear()

# 通过标签名的老爸来定位
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys("APPNIUM")
time.sleep(3)
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").clear()

# 通过标签名的爷爷来定位
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("jetmer")
time.sleep(3)
driver.find_element_by_xpath("//form[@id='form']/span/input").clear()