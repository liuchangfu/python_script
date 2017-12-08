from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://192.168.57.129:8080/zentao/user-login.html")

driver.find_element_by_id("account").send_keys("test01")
driver.find_element_by_name("password").send_keys("11111")
driver.find_element_by_id("submit").click()
time.sleep(3)
'''获取alert对话框'''
alert = driver.switch_to.alert
#打印警告对话框内容
print(alert.text)
#接受弹窗
alert.accept()