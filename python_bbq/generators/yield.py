def foo(n):

    for i in range(5):
        yield i

gen = foo(5)
for i in gen:
    print(i)