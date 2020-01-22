import concurrent.futures as cf
from time import sleep

# a function to multiply 100 numbers. For which operation it needs 0.05
# compare calculation time of multiprocessing map with normal map


def is_prime(x):
    if x >= 2:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    with cf.ThreadPoolExecutor() as executor:
        futures = executor.map(is_prime, list(range(2, 100)))

    for i in futures:
        print(i)



