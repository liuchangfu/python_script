import requests
'''
原文地址：http://blog.csdn.net/shanzhizi/article/details/50903748
r.status_code #响应状态码
r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#*特殊方法*#
r.json() #Requests中内置的JSON解码器
r.raise_for_status() #失败请求(非200响应)抛出异常
'''
#通过GET方法获取接口内容
r = requests.get('http://www.weather.com.cn/data/sk/101280101.html')

#转码成utf-8格式
r.encoding = 'utf-8'

#返回接口地址状态
print(r.status_code)
#打印接口地址url
print(r.url)

print(r.text)
# 转换成json格式
r_json = r.json()
print(r_json)
print(r_json['weatherinfo']['city'])
if r_json['weatherinfo']['city'] == '广州':
    print('Pass!!')
else:
    print('Fail')

