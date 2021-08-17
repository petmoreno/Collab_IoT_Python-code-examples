import threading

class Test:
    
    def __init__(self, j):
        self.a=j

    def Print(self):
        for i in range(100):
            print(self.a, end='')


t1=Test(1)
t2=Test(2)
t3=Test(3)
t4=Test(4)

thread1=threading.Thread(target=t1.Print, daemon=True)
thread2=threading.Thread(target=t2.Print, daemon=True)
thread3=threading.Thread(target=t3.Print, daemon=True)
thread4=threading.Thread(target=t4.Print, daemon=True)

print('Main: set the priorities')

#Setting priorities: WARNING python does not support assining priorities to thread


print('Main: start threads')

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print('Main ready')


