'''
构造方法：
Event()

实例方法：
　　isSet(): 当内置标志为True时返回True。
　　set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
　　clear(): 将标志设为False。
　　wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。
'''

import threading
import time

event  = threading.Event()

def func():
    # 等待事件，进入等待阻塞状态
    print('%s wait forn event...' % threading.current_thread().getName())
    event.wait()
    # 收到事件后进入运行状态
    print('%s recv event.'% threading.current_thread().getName())
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)
# 发送事件通知
print('MainTread set event.')
event.set()