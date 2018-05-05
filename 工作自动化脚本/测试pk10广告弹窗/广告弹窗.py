"""
测试pk10彩种，每个页面打开是否会广告弹窗

"""
import time
from selenium import webdriver
import os
import HTMLTestRunner
import unittest

# 初始化测试网址
# url = 'http://csj.web4.1396c.com//pk10//'
url = 'https://www.1393p.com//pk10//'

# 定义列表存储pk10中所有功能页面链接地址
url_list = ['index', "kaijiang", 'shipin', 'opencodeanalysis', 'coldhotnumber', 'numberrulestat', 'gyhomit', 'ballstat',
            'yilou', 'merge', 'changlongdaystat', 'omitdata', 'specialformdata', 'numpositionalarm', 'twosidedstat',
            'jiqiao', 'luzhuanalysis', 'luzhubigorsmall', 'luzhulonghu', 'guanyahestat', 'luzhuleftorright',
            'bsoetrend', 'zoushitu', 'positiontrend', 'numbertrend', 'guanyatrend', 'positionanalyze', 'betgame',
            'passplan', 'shdd', 'betmode', 'nineplan']

# 列表循环获取网链接地址，打开成功后，并保存载图
for i in url_list:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url + i)
    # driver.get("http://csj.web4.1396c.com//pk10//kaijiang")
    time.sleep(3)

    # 当前脚本存放的真实路径
    cur_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    # print(cur_path)

    # 截图所在的images文件夹
    images_path = os.path.join(cur_path, 'images')

    # 查找是有否images文件夹，没有则自动创建一个
    if not os.path.exists(images_path):
        os.mkdir(images_path)

    # 保存截图到所在的目录
    driver.get_screenshot_as_file("%s\\%s.png" % (images_path, i))

    driver.quit()
