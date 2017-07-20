from time import ctime,sleep
import  threading
def music():
    for i in range(2):
        print('I was listenging to music.%s' % ctime())
        sleep(1)

def move():
    for i in range(2):
        print('I was at the movies! %s' % ctime())
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print('all over %s'% ctime())


def music1(func):
    for i in range(2):
        print('I was listenging to %s.%s' % (func,ctime()))
        sleep(1)


def move1(func):
    for i in range(2):
        print('I was at the %s %s' % (func,ctime()))
        sleep(5)

if __name__ == '__main__':
    music1('爱情卖买')
    move1('金瓶梅')
    print('all over %s'% ctime())


