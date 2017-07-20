from time import ctime,sleep
import threading #导入threading

def music(func):
    for i in range(2):
        print('I was listenging to %s.%s' % (func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print('I was at the %s %s' % (func,ctime()))
        sleep(5)
'''
创建了threads数组，创建线程t1,使用threading.Thread()方法，在这个方法中调用music方法target=music，
args方法对music进行传参。 把创建好的线程t1装到threads数组中,接着以同样的方式创建线程t2，并把t2也装到threads数组。
'''
threads = []
t1 = threading.Thread(target=music,args=('爱情卖买',))
threads.append(t1)

t2 = threading.Thread(target=move,args=('金瓶梅',))
threads.append(t2)
'''
setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，
直接就退出了，同时子线程也一同结束。
'''
if __name__ == '__main__':
    for t in threads: #for循环遍历数组。（数组被装载了t1和t2两个线程）
        t.setDaemon(True)
        t.start() #开始线程活动
    t.join()#在子线程完成运行之前，这个子线程的父线程将一直被阻塞
    print('all over %s'% ctime())

