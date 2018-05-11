import os
import configparser
import sys
import codecs

# 获取当前目录下中的配置文件
ConfigPath = os.path.join(os.getcwd(), os.listdir()[0])

# class ReadConfig():
#     def __init__(self):
#         self.config = configparser.ConfigParser()
#         self.config.read(ConfigPath)
#         # self.config.read("config.ini")
#
#     def get_url(self,name):
#         self.url = self.config.get("Url_Config",name)
#         print(self.url)
#         return self.url

def get_url(name):
    config = configparser.ConfigParser()
    config.read("E:\python_script\AutoTest\Api\Cqssc_api\config\config.ini")
    # config.read(ConfigPath)
    # print(ConfigPath)
    url = config.get("Url_Config", name)
    return url

