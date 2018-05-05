# a = [1,2,3,4]
# # b = a
# # print(a)
# # print(b)

# import copy
# a = [1, 2, 3, 4, [5, 6]]
# d =copy.deepcopy(a)
# print(a)
# print(d)
# print('*'*20)
# a.append(5)
# print(a)
# print(d)
# print('*'*20)
# a[4].append(7)
# print(a)
# print(d)

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# for k,v in enumerate(goods,1):
#     print(k,v)


for k,v in enumerate(goods,1):
    print(k,goods[k-1]["name"],goods[k-1]["price"])

#
# i = int(input('ID:'))
# if i in goods:
#     print(goods[i])
#
# # print(goods[0]['name'])
# # print(goods[0]['price'])
# # print(goods[1])
# # print(goods[2])
# # print(goods[3])
#
# while True:
#     num = input("Input number:")
#
#     print(num.isnumeric())
