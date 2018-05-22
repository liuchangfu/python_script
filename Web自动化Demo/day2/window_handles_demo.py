# _*_ coding:utf-8 _*_
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://bj.ganji.com")
driver.implicitly_wait(5)
# 打印当前句柄
handles = driver.current_window_handle
print(handles)
# 打印所有窗口句柄
driver.find_element_by_link_text("房产").click()
all_handel = driver.window_handles
# 返回一个列表
print(all_handel)
# 切换句柄
driver.switch_to.window(all_handel[1])
print(driver.title)
driver.switch_to.window(handles)
print(driver.title)