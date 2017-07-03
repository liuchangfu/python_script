#格式化打印信息
name = input('请输入姓名：')

age = input('请输入年龄:')

job = input('请输入职业:')

salary = input('请输入工资：')

print ('''
个人信息为: %s
        名字为：%s
        年龄为: %s
        职业为：%s
        工资为：%s
''' % (name,name,age,job,salary))