import requests

url = "http://localhost:12306/"

headers = {
    'cache-control': "no-cache",
    'postman-token': "511063b8-e867-95c6-9339-b19c9118b385"
    }

response = requests.request("GET", url, headers=headers)

res = response.text

print(res)

if res == "mock server started1":
    print('Test Pass!!')
else:
    print('Test faild')