# # NameError错误类型
# try:
#     print (a)
# except NameError :
#     print('打印的变量不存！！')
#
# #打印IndexError错误类型
# try:
#     dict = [1,2,3,4]
#     dict[5]
# except IndexError as e:
#     print(e)
#
# #KeyError错误类型
# try:
#     dict1 = {'k1':'v1'}
#     dict1['k20']
# except KeyError as e:
#     print('你输入的%s值不存在' %e)
#
# #ValueError错误类型
# s1 = 'Hello'
# try:
#     int(s1)
# except ValueError as e:
#     print(e)
#
# # 未捕获到异常，程序直接报错
# s2 = 'Hello'
# try:
#     int(s2)
# except IndexError as e:
#     print(e)

# #出现的任意异常
# s3 = 'hello'
# try:
#     int(s3)
# except IndexError as e:
#     print (e)
# except KeyError as e:
#     print (e)
# except ValueError as e:
#     print (e)

# #万能异常：Exception
# s3 = 'hello'
# try:
#     int(s3)
# except Exception as e:
#     print(e)
#
# #异常其他结构
# try:
#     # 主代码块
#     pass
# except KeyError as e:
#     # 异常时，执行该块
#     pass
# else:
#     # 主代码块执行完，执行该块
#     pass
# finally:
#     # 无论异常与否，最终执行该块
#     pass
#
# #主动触发异常
# try:
#      raise Exception('错误了..')
# except Exception as e:
#     print(e)

#自定义异常

class ChangeException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise ChangeException('我的异常')
except ChangeException as e:
    print(e)