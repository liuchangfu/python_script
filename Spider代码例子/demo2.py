from multiprocessing import Pool
import os, time, random


def run_tast(name):
    print('Task %s (pid = %s) is running!!!!' %(name,os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=4)
    for i in range(5):
        p.apply_async(run_tast, args=(i,))
    print('Waiting for all subprocesses done.')
    p.close()
    p.join()
    print('All subprocesses done!!')
