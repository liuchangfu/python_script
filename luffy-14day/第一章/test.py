# user_list = [['user1','123456'],['user2','123456']]
#
# for each_list in user_list:
#     if isinstance(each_list, list):  #判断当前元素是不是列表
#         for new_each in each_list:
#             print(new_each)
#     else:
#         print(each_list);

username='user1'

f =open('user_lock.txt','r+')
f_lock=f.read()
f.close()
if username in f_lock:
    print('用户名已锁定！！')