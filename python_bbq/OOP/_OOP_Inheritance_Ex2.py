class A:

    def a(self):

        print('a')


class B:

    def a(self):

        print('b')


class C(B, A):   # if C(A, B) -> "a"

    def c(self):
        self.a()


o = C()
o.c()