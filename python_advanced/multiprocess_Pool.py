# Anmerkung zu gestern
# x = [1, 2, 3]
# y = [4, 5, 6, 7]
# def my_sum(a, b):
#     return a+b
# result = map(my_sum, x, y)
# print(list(result))


from time import time, sleep
from multiprocessing import Pool, current_process
import os


def func(n):
    sleep(0.05)
    # return os.getpid()
    # multiprocessing.current_process().pid und os.getpid() geben beide die ID des laufenden prozesses wieder
    return (current_process().pid, os.getpid())

def my_sum(a, b):
    return a+b

# hilfsfunktion um ein element auf mehrere aufzuteilen (ein Tuple in die elemente des Tuples spalten), da bei Pool.map nur ein element übergeben werden kann
def sum_help(t):
    return my_sum(t[0], t[1])

if __name__ == '__main__':
    print('Number of CPUs:', os.cpu_count())
    print()

    t = time()
    # standard map führt die funktion für jedes element des iterables im gleichen prozess aus
    result2 = list(map(func, range(1, 11)))
    print('Seriell:', time()-t)

    p = Pool()
    t = time()
    # Pool.map -> verteilt die berechnung der funktion auf verschiedene prozesse (prozessoren)
    # chunksize hackt das iterable in stücke (kann bei lange iterables die geschwindigkeit erhöhen)
    result = p.map(func, range(1, 11))
    print('Parallel:', time()-t)

    print(result2)
    print(result)
    print()

    p = Pool()
    # übergabe von zwei argumenten durch hilfsfunktion
    # Pool.map akzeptiert nur ein iterable
    result = p.map(sum_help, zip(range(1, 21), range(20, 41)))
    print(result)
