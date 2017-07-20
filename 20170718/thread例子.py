import threading
import time

def worker(num):
    time.sleep(1)
    print('The number is %d' % num)
    return

for i in range(20):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
    t.join()