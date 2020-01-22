from time import time, sleep
from multiprocessing import Process, current_process

def func(x):
    sleep(2)
    print(f'{x} squares to {x*x}')
    print(f'{current_process().name} has ID: {current_process().pid}')


# if __name__ == '__main__':
    #
    # nums = [1, 2, 3, 4, 5]
    #
    # # Seriell:
    # t = time()
    # for num in nums:
    #     func(num)
    # print()
    # print('Seriell:', time()-t)
    #
    # # Parallel:
    # t = time()
    # processes = []
    # for num in nums:
    #     process = Process(target = func, args = (num, ))
    #     processes.append(process)
    #     process.start()
    #
    # for process in processes:
    #     process.join()
    #
    # print()
    # print('Parallel:', time()-t)


# Aufgabe:
# Erstelle eine Funktion, die a+b ausgibt (print()) - und dafür 1 sekunde benötigt
# erstelle für jede berechnung einen prozess

# Bonus: stelle sicher, daß immer nur so viele Prozesse gleichzeitig ausgeführt werden, wie CPUs vorhanden sind
# def my_sum(a, b):
#     sleep(1)
#     print(f"{current_process().name} adds {a}+{b}={a+b}")
#
# if __name__ == '__main__':
#     a = range(10)
#     b = range(10, 20)
#
#     for tup in zip(a, b):
#         my_sum(tup[0], tup[1])
#
#     print()
#     processes = []
#     for tup in zip(a, b):
#         # process = Process(target = my_sum, (tup[0], tup[1]))
#         process = Process(target = my_sum, args = tup)
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     print()
#
#     processes = []
#     for i in range(10):
#         process = Process(target = my_sum, args = (a[i],b[i]))
#         processes.append(process)
#         process.start()
#         if len(processes) >= 2:
#             for p in processes:
#                 p.join()
#             processes = []
#
#     for p in processes:
#         p.join()


if __name__ == '__main__':
    p = Process(target = sleep, args = (5,))

    p.start()
    # bricht den prozess 'p' ab
    p.terminate()
    p.join()

    print('ende')
