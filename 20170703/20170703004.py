import re
print(re.match('www','www.runoob.com').group())
print(re.match('com','www.runoob.com'))

print(re.findall('ab*','cabb3abcbbac'))

print(re.findall("ab+","ab+cd+abb+bba"))

print(re.findall('ab{1,3}','abb abc abbcbbb'))

print(re.search("abc|ABC","ABCBabcCD").group())

print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city"))