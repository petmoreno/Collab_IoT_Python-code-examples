import threading
import time

def WorkerThreadMethod1():
    print("thread 1 started")

    for i in range(100):
        print('1',end='')
        time.sleep(0.001)

def WorkerThreadMethod2():
    print("thread 2 started")

    for i in range(100):
        print('2',end='')
        time.sleep(0.001)


print('Main - create thread')

t1=threading.Thread(target=WorkerThreadMethod1, daemon=True)
t2=threading.Thread(target=WorkerThreadMethod2, daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()