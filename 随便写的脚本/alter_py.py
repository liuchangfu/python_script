from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///E:/python%E8%84%9A%E6%9C%AC/%E9%9A%8F%E4%BE%BF%E5%86%99%E7%9A%84%E8%84%9A%E6%9C%AC/alter.html")
'''获取alert对话框的按钮,点击按钮,弹出alert对话框'''
driver.find_element_by_xpath("/html/body/div/input[2]").click()
'''获取alert对话框'''
alter = driver.switch_to.alert
time.sleep(2)
'''获取警告对话框的内容'''
print(alter.text) #打印警告对话框内容
alter.accept()  #alert对话框属于警告对话框，我们这里只能接受弹窗
time.sleep(2)
driver.quit()
