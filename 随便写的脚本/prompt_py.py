from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get("file:///E:/python%E8%84%9A%E6%9C%AC/%E9%9A%8F%E4%BE%BF%E5%86%99%E7%9A%84%E8%84%9A%E6%9C%AC/alter.html")
driver.find_element_by_xpath("/html/body/div/input[1]").click()
'''获取prompt对话框'''
dialog_box = driver.switch_to.alert
time.sleep(2)
print(dialog_box.text)
'''获取对话框输入1，并且点击【确认】,文本框内提示<左哥是真笨啊>'''
dialog_box.send_keys("1")
dialog_box.accept()
print(driver.find_element_by_xpath("//*[@id='textSpan']/font").text)

'''获取对话框输入2，并且点击【确认】,文本框内提示<左哥是真笨啊>'''
driver.find_element_by_xpath("/html/body/div/input[1]").click()
'''获取prompt对话框'''
dialog_box = driver.switch_to.alert
time.sleep(2)
print(dialog_box.text)
dialog_box.send_keys("2")
dialog_box.accept()
print(driver.find_element_by_xpath("//*[@id='textSpan']/font").text)

'''获取对话框,点击【取消】文本框内提示<您没有按要求输入，请重新输入>'''
driver.find_element_by_xpath("/html/body/div/input[1]").click()
'''获取prompt对话框'''
dialog_box = driver.switch_to.alert
time.sleep(2)
dialog_box.dismiss()
print(driver.find_element_by_xpath("//*[@id='textSpan']/font").text)
time.sleep(2)
