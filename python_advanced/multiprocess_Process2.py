from time import time, sleep
from multiprocessing import Process, current_process
import os, platform

a = range(10)
b = range(10, 20)


def func():
    sleep(1)
    result = map(sum, zip(a, b))
    print(f'{result}')
    print(f'{current_process().name} has ID: {current_process().pid} and runs on {platform.processor()}')


if __name__ == '__main__':
    nums = [i for i in range(1, 10)]

    # Serial
    t = time()
    for num in nums:
        func()
    print()
    print('Seriell:', time()-t)


    # Concurrent:
    t = time()
    processes = []
    for num in nums:
        process = Process(target=func)
        processes.append(process)
        process.start()
    # if there are more than 2 processes (in the list), do not proceed
        if len(processes) >= 2:
            for p in processes:
                p.join()
            process = []

    for p in processes:
        p.join()

    print()
    print('Concurrent:', time()-t)

