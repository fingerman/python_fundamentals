def is_prime(x):
    if x >= 2:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        return True
    else:
        return False


def cal(liste):
    primes_list = []
    for i in range(liste[0], liste[1]+1):
        if is_prime(i):
            primes_list.append(i)
    return primes_list


def inp():
    s = int(input("Define Start: "))
    e = int(input("Define End: "))
    return [s, e]


def out():
    print(" ".join(map(str, cal(inp()))))


out()