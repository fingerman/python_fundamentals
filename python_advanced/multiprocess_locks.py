from multiprocessing import Process, Lock, Value

def p2_noLock(v):
    v.value += 2

def m2_noLock(v):
    v.value -= 2

def p2_Lock(v, lock):
    lock.acquire()
    v.value += 2
    lock.release()

def m2_Lock(v, lock):
    with lock:
        v.value -= 2



if __name__ == '__main__':
    v_noLock = Value('i', 100)
    v_Lock = Value('i', 100)
    processes = []
    # ohne Lock()
    for i in range(20):
        p_p2_noLock = Process(target = p2_noLock, args = (v_noLock,))
        p_m2_noLock = Process(target = m2_noLock, args = (v_noLock,))

        p_p2_noLock.start()
        p_m2_noLock.start()

        processes.append(p_p2_noLock)
        processes.append(p_m2_noLock)

    # mit Lock
    lock = Lock()
    for i in range(20):
        p_p2_Lock = Process(target = p2_Lock,
                            args = (v_Lock, lock))
        p_m2_Lock = Process(target = m2_Lock,
                            args = (v_Lock, lock))

        p_p2_Lock.start()
        p_m2_Lock.start()

        processes.append(p_p2_Lock)
        processes.append(p_m2_Lock)

    for process in processes:
        process.join()

    print('No Lock:', v_noLock.value)
    print('Lock:', v_Lock.value)
