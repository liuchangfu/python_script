# import demjson
#
# a =  [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#
# json1 = demjson.encode(a)
#
# print(json1)
#
# b = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
#
# json2 = demjson.decode(b)
#
# print(json2)

import json
a={
    "_class": "hudson.model.Hudson",
    "jobs":
         [
        {
            "_class": "com.tikal.jenkins.plugins.multijob.MultiJobProject",
            "name": "fisrt_job"
        },
        {
            "_class": "hudson.model.FreeStyleProject",
            "name": "second_job"
        }
        ]
}

a_js  = json.dumps(a)

print(a["jobs"][0]["name"])
print(a["jobs"][1]["name"])