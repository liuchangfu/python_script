# _*_ coding:utf-8 _*_

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys("测试部落")
driver.find_element_by_id("su").click()
ele = driver.find_elements_by_css_selector(".t>a")
for i in ele:
    print(i.get_attribute("href"))