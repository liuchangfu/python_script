menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

# 普通版
while True:
    for k in menu:
        print(k)
    choice = input(">1").strip() #输入第一层
    if not choice:continue
    if choice in menu:
        while True:
            for k in menu[choice]:
                print(k)
            choice2 = input(">>2").strip() # 输入第二层
            if not choice2:continue
            if choice2 in menu[choice]:
                print(menu[choice][choice2])
                while True:
                    for k in menu[choice][choice2]:
                        print(k)
                    choice3 = input(">>>3").strip() #输入第三层
                    if not choice3:continue
                    if choice3 in menu[choice][choice2]:
                        print(menu[choice][choice2][choice3])
                        while True:
                            choice4 = input(">>>>4").strip() # 输入第四层
                            if not choice4:continue
                            if choice4 in menu[choice][choice2][choice3]:
                                    print(menu[choice][choice2][choice3][choice4])
                            elif choice4 == 'b':
                                break
                            elif choice4 == 'q':
                                exit()
                            else:
                                print('该节点不存在，请重新输入！！')
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit()
                    else:
                        print('该节点不存在，请重新输入！！')
            elif choice2 =='b':
                break
            elif choice2 == 'q':
                exit()
            else:
                print('该节占不存在，请重新输入！！')
    elif choice =='b' :
        print('已经回退到第一级啦！！')
    elif choice == 'q':
        exit()
    else:
        print('该节点不存在，请重新输入！！')
