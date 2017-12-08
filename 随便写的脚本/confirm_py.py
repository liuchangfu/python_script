from selenium import webdriver
import time

driver =webdriver.Chrome()

driver.get("file:///E:/python%E8%84%9A%E6%9C%AC/%E9%9A%8F%E4%BE%BF%E5%86%99%E7%9A%84%E8%84%9A%E6%9C%AC/alter.html")
'''获取confirm对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath("/html/body/div/input[3]").click()
'''获取confirm对话框'''
dialog_box = driver.switch_to.alert
time.sleep(2)
'''获取对话框的内容'''
print(dialog_box.text) #打印警告对话框内容
dialog_box.accept()  #接受弹窗
#打印接受对话框后的提示信息
print(driver.find_element_by_xpath("//*[@id='textSpan']/font").text)


driver.find_element_by_xpath("/html/body/div/input[3]").click()
dialog_box = driver.switch_to.alert
time.sleep(2)
dialog_box.dismiss()  #关闭获取取消对话框
print(driver.find_element_by_xpath("//*[@id='textSpan']/font").text)