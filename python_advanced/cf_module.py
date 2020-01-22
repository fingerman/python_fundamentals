import concurrent.futures as cf
from time import sleep


def mult(a, b):
    sleep(0.02)
    return a * b


if __name__ == '__main__':
    with cf.ProcessPoolExecutor(max_workers=2) as executor:
        future = executor.submit(mult, 5, 6)

    print(future.result())

    with cf.ThreadPoolExecutor() as executor:
        future = executor.map(mult, (5, 6, 5), (5, 6, 5, 8))

    print(list(future))
