from time import time, sleep
from multiprocessing import Process, current_process
import os


def func(x):
    sleep(0.08)
    print(f'{x} squares to {x*x}')
    print(f'{current_process().name} has ID: {current_process().pid}')


if __name__ == '__main__':
    nums = [i for i in range(1, 10)]

    # Serial
    t = time()
    for num in nums:
        func(num)
    print()
    print('Seriell:', time()-t)


    # Concurrent:
    t = time()
    processes = []
    for num in nums:
        process = Process(target=func, args = (num, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print()
    print('Concurrent:', time()-t)


#