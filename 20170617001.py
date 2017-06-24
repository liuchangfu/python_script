#输入字典的值，并打印，如果不存在，退出

dict1 = {
    'name':'Change',
    'tel':18620059772,
    'address':'Guangzhou',
    'job':'IT',
    'age':30
}

while True:
    str1 = input('请输入你要查找的信息:')
    if str1 in dict1:
        print('查询结果为:',dict1[str1])
        break
    else:
        print('你要查找的信息不存在!!')
        continue

