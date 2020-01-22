from time import sleep
from multiprocessing import Process, Queue, current_process


class Timer:
    import time

    def __enter__(self):
            self.start = Timer.time.time()

    def __exit__(self, type = None, value = None, traceback = None):
        self.end = Timer.time.time()-self.start
        print(self.end)

def putX(q, x):
    for i in x:
        sleep(0.01)
        q.put(i)

def getX(q):
    while True:
        sleep(0.1)
        if q.full():
            element = q.get()
            print(element)

if __name__ == '__main__':

    q = Queue(maxsize = 5)

    p1 = Process(target = putX, args = (q, range(20)))
    p2 = Process(target = getX, args = [q])


    p1.start()
    p2.start()


    p1.join()


    print('processes - end')
    while not q.empty():
        print(q.get())

    # p2 läuft in endlosschleife muß gewaltsam terminiert werden
    p2.terminate()
    sleep(0.01)
    # das schließen von p2 dauert länger, als der aufruf (is_alive), deshalb kurzes delay
    print(p2.is_alive())

    # timeout: wenn get kein element innerhalb von 'timeout' sekunden erhält, dann wirft es eine 'Empty' exception
    try:
        q.get(timeout = 3)
    except Exception as e:
        print(e.__class__.__name__)
        print(type(e))
    print('programm ending')
