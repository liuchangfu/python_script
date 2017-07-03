def stu_register(name, age, country, course,**kwargs):
    print("----注册学生信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)
    print('职位：',kwargs)


stu_register("王山炮", 22, "CN", "python_devops",job='it',pr='湖南')
