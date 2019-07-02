# A lock allows only one thread to enter the part that's locked and the lock is not shared with any other processes.
#
# A mutex is the same as a lock but it can be system wide (shared by multiple processes).
#
# A semaphore does the same as a mutex but allows x number of threads to enter,
# this can be used for example to limit the number of cpu,
# io or ram intensive tasks running at the same time.



import threading

semaphore = threading.Semaphore(3)

def f1():
    semaphore.acquire()
    print(semaphore)
    print("%s acquired lock." % (threading.current_thread().name))
    print(semaphore._value)
    semaphore.release()
    # semaphore.release()
    print("%s released lock." % (threading.current_thread().name))
    print(semaphore._value)

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f1)
t1.start()
t2.start()

print("Main thread exited.", threading.main_thread())
