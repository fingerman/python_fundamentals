import concurrent.futures as cf
from time import sleep
import threading as td


def mult(x, y):
    sleep(0.02)
    print(td.current_thread().name)
    return x*y

if __name__ == '__main__':
    with cf.ProcessPoolExecutor(max_workers=2) as executor:
        future = executor.submit(mult, 5, 6)

    print(future.result())

    with cf.ThreadPoolExecutor() as executor:
        future = executor.map(mult, (5, ), [6])


    print(list(future))

    for f in future:
        print(f)



