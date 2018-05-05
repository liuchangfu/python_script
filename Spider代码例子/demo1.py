import os
from multiprocessing import Process


def run_prco(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_prco, args=(str(i),))
        print('process will start.')
        p.start()
    p.join()
    print('process end.')
