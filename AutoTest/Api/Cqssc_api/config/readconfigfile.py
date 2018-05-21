# _*_ coding:utf-8 _*_
import os
import configparser
import codecs


# 获取当前目录下中的配置文件
Path = os.path.join(os.getcwd(), os.listdir()[0])
print(Path)


# class ReadConfig():
#     def __init__(self):
#         self.config = configparser.ConfigParser()
#         self.config.read(ConfigPath)
#
#
#     def get_url(self,name):
#         self.url = self.config.get("Url_Config",name)
#         print(self.url)
#         return self.url

def get_url(name):
    config = configparser.ConfigParser()
    config.read(Path)
    # with open(Path, 'r', encoding="utf-8-sig8") as cfg:
    #     config.readfp(cfg)
    # config.readfp(codecs.open(Path, "r", "gbk"))
    url = config.get("HTTP", name)
    return url


# res = get_url("baseurl")
# print(res)
