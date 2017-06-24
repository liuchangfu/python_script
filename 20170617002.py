#定义购物清单
list1 = [
    ('iPhone',6500),
    ('bike',1000),
    ('coffe',50),
    ('pythonbook',100)
]
# 定义空列表，用于存储购物后商品
buy_list = []
salary = input("请输入您的预算:")
if salary.isdigit()
    salary = int(salary)
    while True:
        for index,item in enumerate(list1):
            print(index,item)
        user_choice = input('请输入你要购买的商品:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice <= len(list1) and user_choice>= 0:
                p_item = list1[user_choice]
                if p_item[1] <= salary:
                    buy_list.append(p_item)
                    salary = salary-p_item[1]
                    print('您选的商品为%s，价钱为 %s' % (buy_list,salary))
                else:
                    print ('余额不足，您的余额为%s！！' % salary)
            else:
                print('商品不存在！')
        elif user_choice == 'q':
            print('-----购物清单-----')
            for p in buy_list:
                print(p)
            print(salary)
            exit()
        else:
            print('无效!!')

