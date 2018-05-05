import os
import unittest
import time
import HTMLTestRunner

# 当前脚本存放的真实路径
cur_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

# 用例文件夹
case_path = os.path.join(cur_path, 'case')

# 如果不存case文件夹，自动创建一个
if not os.path.exists(case_path):
    os.mkdir(cur_path)

# 测试报告文件夹
report_path = os.path.join(cur_path, 'report')

# 如果不存report文件夹，自动创建一个
if not os.path.exists(report_path):
    os.mkdir(report_path)

# 定义discover方法，加载所有测试用例
discover = unittest.defaultTestLoader.discover(
    case_path, pattern='test*.py', top_level_dir=None)

if __name__ == '__main__':
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

# 定义测试报告路径
report_abspath = os.path.join(report_path, now + "_result.html")

# 写入测试结果至测试报告所在目录
fp = open(report_abspath, 'wb')

# 生成测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp, title='重庆时时彩接口测试结果', description='用例执行结果')

# 运行测试用例
runner.run(discover)

# 关闭文件
fp.close()
