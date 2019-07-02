import threading
import time

# Asynchronous Tasks; Some Tasks can take a while; Ex: Input and Output takes a while.
# Some programs are req. to be in real time. We can setup threads to run in the background,
# to write a file or search for items, while user can still interact with the interface/commandline.

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self) # superclass
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out,'a')
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("Finished Background File Write to " + self.out)

def Main():
    message = input("Enter string to store: ")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program can continue while it writes in another thread.")
    print("100 + 400 = ", 100+ 400)

    background.join()
    print("Waited until thread was complete.")

if __name__ == '__main__':
    Main()