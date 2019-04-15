class FibIterator:
    def fibo(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.fibo(x-1) + self.fibo(x-2)


f = FibIterator()

for i in range(16):
    print(f.fibo(i))
