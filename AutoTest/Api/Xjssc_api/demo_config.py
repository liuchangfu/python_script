"""
configparser模块

1) 基本的读取配置文件
     -read(filename) 直接读取ini文件内容
     -sections() 得到所有的section，并以列表的形式返回
     -options(section) 得到该section的所有option
     -items(section) 得到该section的所有键值对
     -get(section,option) 得到section中option的值，返回为string类型
     -getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。

2) 基本的写入配置文件
     -add_section(section) 添加一个新的section
     -set( section, option, value) 对section中的option进行设置，需要调用write将内容写入配置文件。
"""
import configparser

# 实例化对象
conf = configparser.ConfigParser()

# 打开配置文件
conf.read('config.ini')

# 获取配置文件所有节点
secs = conf.sections()
print('secs:', secs)

#  返回该website的所有键值对
secs1 = conf.items('website')
print('secs1:', secs1)

# 获取配置文件相应的节点的配置参数
ops = conf.options('website')
print('ops:', ops)

# 获取配置文件下相应节点的值
url = conf.get('website', 'url')
print(url)

versoin = conf.get('version', 'version')
print(versoin)

# https://mo.1394x.com/xjssc/BetGame?version=3000
add_url = url + '/' + '/xjssc/BetGame' + '?' + 'versoin=' + versoin
print(add_url)
