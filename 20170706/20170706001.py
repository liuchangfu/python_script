from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()

browser.implicitly_wait(30)

browser.get('http://www.baidu.com')

browser.quit()