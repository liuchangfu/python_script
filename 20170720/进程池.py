from multiprocessing import Process,Pool,freeze_support
import time


def Foo(i):
    time.sleep(2)
    return i+100

def Bar(arg):
    print('--->exec done',arg)

if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)

    print('end')
    pool.close()
    pool.join()