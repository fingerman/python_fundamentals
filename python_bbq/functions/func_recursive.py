def count(n):
    if n >= 1:
        print(n)
        count(n - 1)


count(5)
