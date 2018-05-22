# _*_ coding:utf-8 _*_
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# xpath逻辑运算
driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").send_keys("python")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").clear()

# 模糊匹配
driver.find_element_by_xpath("//a[contains(.,'hao123')]").click()

# 模糊匹配某个属性
driver.find_element_by_xpath("//input[contains(@id,'kw')]").send_keys("AAA")
time.sleep(3)
driver.find_element_by_xpath("//input[contains(@id,'kw')]").clear()

# 模糊匹配以什么结尾的属性
driver.find_element_by_xpath("//input[contains(@class,'ipt')]").send_keys("BBBB")
time.sleep(3)
driver.find_element_by_xpath("//input[contains(@class,'ipt')]").clear()

# 模糊匹配以什么开头的属性
driver.find_element_by_xpath("//input[contains(@class,'s_i')]").send_keys("CCC")
time.sleep(3)
driver.find_element_by_xpath("//input[contains(@class,'s_i')]").clear()
