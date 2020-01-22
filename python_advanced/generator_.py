#
# # generator funktion
# def sqr_num_gen(nums):
#     for i in nums:
#         # wenn yield aufgerufen wird, dann wird der wert i*i zurückgegeben und die funktion gestoppt
#         # wenn die funktion mit dem nächsten next() aufgerufen wrid, dann geht direkt nach dem yield statement weiter
#         yield i*i
#
#
# l = [1,2,3]
#
# gen_func = sqr_num_gen(l)
#
# print(next(gen_func))
# print(next(gen_func))
#
# print()
#
# def sqr_num_gen2():
#     nums = [1,2,3]
#     for i in nums:
#         yield i*i
#
#     print('Schleife Ende')
#
# gen_func = sqr_num_gen2()
#
# for i in gen_func:
#     print(i)
#
# print(type(gen_func))
#
#
# def yield_test():
#     yield '1'
#     print('nach yield 1')
#     yield 'hallo'
#     print('nach yield 2')
#     yield 34
# #
# #
# # test = yield_test()
# #
# # print(next(test))
# # print('-------')
# # print(next(test))
#
# # x == generator objekt
# x = (i*i for i in l)
#
# print(type(x))
# # x == liste
# x = [i*i for i in l]
#
# print(type(x))
#
# #
# # print(next(x))
# # print(next(x))
# # print(next(x))
#
# # Aufgabe:
# # erstelle einen counter generator, der immer in 0.5 schritten von 0 bis zu einem maximum zählt
#
#
# def my_counter(max):
#     i = 0
#     while i <= max:
#         yield i
#         i += 0.5
#
# count = my_counter(10)
#
# for i in count:
#     print(i)
#
# def my_counter2(min, max):
#     while min <= max:
#         yield min
#         min += 0.5
#
# count = my_counter2(5, 10)
#
# for i in count:
#     print(i)
# print()
# print()

# from time import time
#
# l = list(range(100000))
#
# t = time()
# x = (i*i for i in l)
# print(time()-t)
#
# t = time()
# x = [i*i for i in l]
# print(time()-t)

# endlos coutner
def my_endless_counter(min):
    while True:
        yield min
        min += 0.5


ec = my_endless_counter(10)

# ausgabe des unendlichen counters
# kann in der Konsole mit strg+c abgebrochen werden
# bei python-run (F5) - fenster schließen
for i in ec:
    print(i)
