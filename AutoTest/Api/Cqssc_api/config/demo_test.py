import configparser
import os

config = configparser.ConfigParser()

config.read("config.ini")

url = config.get("Url_Config","baseurl")
print(url)

# path = os.path.join(os.getcwd(), os.listdir()[0])
# def get_url(name):
#     config = configparser.ConfigParser()
#     config.read(path)
#     url = config.get("Url_Config", name)
#     return url
#
#
# res = get_url("baseurl")
# print(res)


# import os
# print("当前目录:",os.getcwd())
# print("当前目录下的文件:",os.listdir())
# path = os.path.join(os.getcwd(), os.listdir()[1])
# print(path)