import requests

response = requests.get('http://www.zhihu.com')



print(response.content)