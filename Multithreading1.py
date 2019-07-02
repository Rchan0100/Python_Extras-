# Threads can be thought of as separate programs running alongside each other.
# Can be used for quick tasks like calc. a result from an alg.
# and also running slow proccesses in the background while the program continues

#Ex: Hashing 100 passwords with md5 h.alg. BUT you can have 5-10 threads to make the total time 5-10x faster.
#Already using one thread (main thread)

# We use locks to lock access to a thread.
# B/c threads may run simultaneously, no guarantee that both threads won't use the same variables.

# When to use Multithreading (Basic)
# Multithreading is good for GUI; One thread for interface, one to do the work in the background.
# No point if running on one core. Threads will be time split on one core.
# Great for servers that deal with TCP connections, as you want to handle more than one request at a time.


import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print(name + " has Started")
    tLock.acquire()
    print(name + " has acquired the lock.")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print(name + " is releasing the lock.")
    tLock.release()
    print("Timer:  "+name+" Completed")

def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main completed.")

if(__name__ == '__main__'):
    Main()

