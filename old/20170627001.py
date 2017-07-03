#文件替换
f = open('e:\\python\\day3','r',encoding='utf-8')

find_text=input('请输入要查找的内容：')
while True:
    for line in f:
            if find_text not in line:
                continue
            else:
                print('你查找的内容为：', line)
                break
f.close()


