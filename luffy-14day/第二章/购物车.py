# 初始化用户名和密码
username = "change"
password = "123456"
inp_username = input('请输入用户名>>>').strip()
inp_password = input('请输入密码>>>').strip()

while True:
    if inp_username == username and inp_password == password:
        account = float(input('请输入初始化金额:'))
        break
    else:
        inp_password = input('密码错误，请重新输入！')
        continue

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
# 定义空列表，存储所选择的商品
goods_staff = []

print("欢迎您登录，你的初始化金额为\033[1;35m %s \033[0m" % account)

while True:
    print('*' * 50)
    for k, v in enumerate(goods, 1):
        print(k, goods[k - 1]["name"], goods[k - 1]["price"])
    index = input('请输入商品编号(输入q或y退出)>>>>')
    if index == "q" or index == 'y':
        print('您所购买的商品为\033[1;35m %s \033[0m,您的余额为\033[1;35m %0.1f \033[0m' % (goods_staff, account))
        break
    elif index.isdigit() == False:
        print("\033[1;35m 商品输入有误!请重新输入>> \033[0m")
        continue
    elif int(index) > len(goods) or int(index) <= 0:
        print("\033[1;35m 商品编号输入有误!!!请重新输入>>>>\033[0m")
        continue
    else:
        index_buy = int(index) - 1
        if goods[index_buy]["price"] < account:
            account = account - goods[0]["price"]
            print("\033[1;35m您已经将%s加入购物车中，余额为%0.1f\033[0m" % (goods[index_buy]["name"], account))
            goods_staff.append(goods[index_buy]["name"])
        else:
            print("\033[1;35m余额不足，无法购买!\033[0m")
