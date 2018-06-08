# _*_ coding:utf-8 _*_
from selenium import webdriver
import time
"""
alert操作思路
    1.先用switch_to_alert()方法切换到alert弹出框上
    2.可以用text方法获取弹出的文本 信息
    3.accept()点击确认按钮
    4.dismiss()相当于点右上角x，取消弹出框

"""
url = "file:///E:/python_script/Web%E8%87%AA%E5%8A%A8%E5%8C%96Demo/day4/alert.html"

driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_id("alert").click()
time.sleep(3)
t = driver.switch_to_alert()
print(t.text)
# t.accept()
t.dismiss()