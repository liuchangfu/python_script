import os
import configparser
import codecs

# 当前配置文件存放的真实路径
# ConfigPath = os.path.abspath(os.curdir) + '\\config.ini'
# 当前脚本存放的真实路径
# RealPath = os.path.join(os.path.dirname(os.path.realpath(__file__)))
# ConfigPath = os.path.join(RealPath,"config")

# config = configparser.ConfigParser()
# config.read(ConfigPath)
#
# url = config.get("HTTP","baseurl")
# print("url:",url)

# print(ConfigPath)

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

def get_url(config_file,name):
    config = configparser.ConfigParser()
    config.read(config_file)
    url = config.get("Url_Config",name)
    return url

# res= get_url("baseurl")
# print(res)