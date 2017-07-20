import multiprocessing
import threading
import time

def thread_run():
    print(threading.get_ident())

def f(name):
    time.sleep(2)
    print('Hello',name)
    t = threading.Thread(target=thread_run,)
    t.start()

if __name__=='__main__':
    for i in range(10):
        p = multiprocessing.Process(target=f,args=('jobs',))
        p.start()
