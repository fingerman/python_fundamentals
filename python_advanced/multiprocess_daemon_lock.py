import threading as td
from time import sleep

class Timer:
    import time

    def __enter__(self):
            self.start = Timer.time.time()

    def __exit__(self, type = None, value = None, traceback = None):
        self.end = Timer.time.time()-self.start
        print(self.end)

def endless():
    while(True):
        sleep(0.01)
        print('Hello World!')


def plus2(lock):
    global y
    for i in range(100):
        with lock:
            y += (2*sum(range(10000)))

def minus2(lock):
    global y
    for i in range(100):
        lock.acquire()
        y -= (2*sum(range(10000)))
        lock.release()

def plus2nl():
    global y
    for i in range(100):
        y +=  (2*sum(range(10000)))

def minus2nl():
    global y
    for i in range(100):
        y -= (2*sum(range(10000)))

y = 0
lock = td.Lock()

t = td.Thread(target = endless, daemon = True)
t.daemon = True
t.start()


with Timer():
    t1 = td.Thread(target = plus2, args = (lock, ))
    t2 = td.Thread(target = minus2, args = (lock, ))
    t1.start()
    t2.start()
    for tr in td.enumerate()[2:]:
        tr.join()

with Timer():
    t1 = td.Thread(target = plus2nl)
    t2 = td.Thread(target = minus2nl)
    t1.start()
    t2.start()

    t1.join()
    t2.join()


print('End')
