# _*_ coding:utf-8 _*_
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 通过id定位
driver.find_element_by_id("kw").send_keys("python")
time.sleep(1)
driver.find_element_by_id("kw").clear()

# 通过name定位
driver.find_element_by_name("wd").send_keys("selenium")
time.sleep(1)
driver.find_element_by_name("wd").clear()

# 通过class定位
driver.find_element_by_class_name("s_ipt").send_keys("jemter")
time.sleep(1)
driver.find_element_by_class_name("s_ipt").clear()

# 通过tag（标签）定位，不推荐使用该方法，真实的网页中，相同标签太多
# driver.find_element_by_tag_name("input").send_keys("lr")

# 通过link（超链接）属性定位
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("hao123").click()
time.sleep(1)

# 通过partial_link模糊匹配方式定位
driver.get("https://www.baidu.com")
driver.find_element_by_partial_link_text("123").click()
time.sleep(1)