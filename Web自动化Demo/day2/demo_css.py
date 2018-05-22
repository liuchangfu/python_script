# _*_ coding:utf-8 _*_
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# # 通过id属性定位
# driver.find_element_by_css_selector("#kw").send_keys("AAAA")
# time.sleep(3)
# driver.find_element_by_css_selector("#kw").clear()
#
# # 通过class属性定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("BBBB")
# time.sleep(3)
# driver.find_element_by_css_selector(".s_ipt").clear()

# # 通过name属性定位
# driver.find_element_by_css_selector("[name='wd']").send_keys("CCCC")
# time.sleep(3)
# driver.find_element_by_css_selector("[name='wd']").clear()

# 通过autocomplete属性来定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("DDDD")
# time.sleep(3)
# driver.find_element_by_css_selector("[autocomplete='off']").clear()

# 通过type属性来定位
# driver.find_element_by_css_selector("[type='text']").send_keys("EEEE")
# time.sleep(3)
# driver.find_element_by_css_selector("[type='text']").clear()

# 通过标签与class属性组合定位
# driver.find_element_by_css_selector("input.s_ipt").send_keys("FFFF")
# time.sleep(3)
# driver.find_element_by_css_selector("input.s_ipt").clear()

# 通过标签与id属性组合定位
# driver.find_element_by_css_selector("input#kw").send_keys("FFFF")
# time.sleep(3)
# driver.find_element_by_css_selector("input#kw").clear()

# 通过标签与name属性组合定位
# driver.find_element_by_css_selector("input[name='wd']").send_keys("GGGG")
# time.sleep(3)
# driver.find_element_by_css_selector("input[name='wd']").clear()

# 通过层级定位
driver.find_element_by_css_selector("form#form>span>input").send_keys("HHHH")
time.sleep(3)
driver.find_element_by_css_selector("form#form>span>input").clear()

