try:
    f = open('我为什么是个文档.txt')
    print(f.read())
    f.close()
except OSError:
    print('文件打开错误！！')
