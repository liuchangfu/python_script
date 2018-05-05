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

# 进阶版
current_layer = menu
layers = []
while True:
    for k in current_layer:
        print(k)
    choice = input('>').strip()
    if not choice:
        continue
    if choice in current_layer:
        layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if layers:
            current_layer = layers.pop()
        if len(layers) == 0:
            print('已经回退到第一级了！！')
    elif choice == 'q':
        exit()
    else:
        print('该节点不存在，请重新输入！！')