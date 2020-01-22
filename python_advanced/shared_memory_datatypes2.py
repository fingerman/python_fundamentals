from multiprocessing import Process, Value


def plus2(v):
    v.value += 2


def minus2(v):
    v.value -= 2


if __name__ == '__main__':
    c = Value('f', 1.0)

    p1 = Process(target=plus2, args=(c,))
    p2 = Process(target=minus2, args=(c,))

    print('Before process:', c.value)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('After process', c.value)
