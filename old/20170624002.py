#文件替换
f = open('e:\\python\\day2.txt','r',encoding='utf-8')

f_new = open('e:\\python\\day2.bak','w',encoding='utf-8')

for line in f:
    if '肆意的快乐等我享受' in line:
        line=line.replace('肆意的快乐等我享受','肆意的快乐等Change享受')

    f_new.write(line)

f.close()
f_new.close()

