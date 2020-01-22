from multiprocessing import Process, Value


def shared_double(v):
    v.value *= 2


def shared_tripple(v):
    v *= 3


if __name__ == '__main__':
    v = Value('f', 1.0)

    p1 = Process(target=shared_double, args=(v,))
    p2 = Process(target=shared_double, args=(v,))

    print('Before process:', v.value)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('After process', v.value)
