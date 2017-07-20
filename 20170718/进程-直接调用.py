import threading
import time
t_start  = time.time()
t_jobs = []
def run(n):
    print('task',n)
    time.sleep(2)
    print('Task done!!')

for i in range(50):
    t = threading.Thread(target=run,args=('Task-%s'% i,))
    t.start()
    t_jobs.append(t)

for t in t_jobs:
    t.join()

print('All threads has finished!!!')
print('count time:',time.time()-t_start)