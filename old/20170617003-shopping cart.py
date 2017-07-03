'''
程序：购物车程序

需求:

启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随时退出，退出时，打印已购买商品和余额

#知识点：len(market):列表长度（列表中的条目个数）
       isdigit() 判断输入的内容是否是数字，TRUE 是数字
       取列表数据 enumerate
       for index,item in enumerate(market)
            print(index, item)
    输出内容高亮显示 "\033[31;1m%s\033[0m"%(balance)
    退出程序使用exit()方法
'''

market = [[1 ,"iphone" ,5800],
          [2 ,"Mac Pro", 12000],
          [3 ,"Starbuck Latte" ,31],
          [4 ,"Alex Python" ,88],
          [5 ,"bike" ,1800]]

balance = input("please input salary: ")
if balance.isdigit():
    balance = int(balance)
else:
    exit("Illegal value, please re-enter")

amount = 0
print("Tip: type q to exit.\n\n")

shopping_cart = []
while True:
    for commodity in market:
        print(commodity)

    user_choice = input("Please enter a product number or q：\n")

    if user_choice == "q":
        break

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 0 < user_choice and user_choice <= (len(market ) +1):
            amount += market[user_choice - 1][2];
            if balance < amount:
                print("Reminder: the balance is insufficient, please re-purchase.\n")
                continue
            shopping_cart.append(market[user_choice - 1])
        else:
            print("If you do not have this item, please reselect it !\n")
            continue

print("List of purchased items:\n")
for commodity in shopping_cart:
    print(commodity)
print( "Payment amount: \033[41;1m%s\033[0m" %(amount))
balance -= amount
print( "your balance: \033[31;1m%s\033[0m \n" %balance)

