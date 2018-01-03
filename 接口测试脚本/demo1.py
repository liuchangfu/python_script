import requests
from requests.auth import HTTPBasicAuth

# # GET
# print(requests.get('http://localhost:8080/job/fisrt_job/disable'))
print(requests.get('http://localhost:8080/api/json?tree=jobs[name]'))

# POST with basic auth
url = 'http://localhost:8080/job/fisrt_job/disable'
r = requests.post(url,data={},auth = ('admin','lcfwku'))
print(r.status_code)
print(r.headers)
print(r.reason)
