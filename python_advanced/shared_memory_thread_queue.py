import queue
import threading as td

def put_in5(q):
    q.put(5)

def put_in_list(l):
    # for i in range(len(l)):
    #     l[i] = 0
    # l.append(10)

    for e in l:
        e = 0

q = queue.Queue()

t = td.Thread(target = put_in5, args=(q, ))
t.start()
t.join()

print(q.get())
print(q.empty())

l = [1, 2, 3]

t = td.Thread(target = put_in_list, args=(l, ))

t.start()
t.join()

print(l)
