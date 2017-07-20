import threading
import queue
q = queue.Queue()
def prod():
    for i in range(10):
        q.put('骨头 %s' % i)
        print('开始等待所有的骨头被取走%s...' %i)
        # q.join()
        # print('所有的骨头的被取完了。。。')


def cons(n):
    while True:
        print('%s取到' %n ,q.get())

p = threading.Thread(target=prod,)
c =  threading.Thread(target=cons,args=('Change',))
p.start()
c.start()
