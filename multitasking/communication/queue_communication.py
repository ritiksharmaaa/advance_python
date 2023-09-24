# quee communication .
from queue import Queue
from threading import Thread
from time import sleep 

class Producer:
    def __init__(self):
        self.q = Queue()

    def Producer(self):
        for i in range(1 , 6):
            print("item produced " , i )
            self.q.put(i)
            sleep(1)



class Consumer:
    def __init__(self , prod):
        self.prod = prod
    def consumer(self):
        for i in range(1, 6):
            print("item recived " , self.prod.q.get(i))


p = Producer()
c = Consumer(p)
t1 = Thread(target=p.Producer)
t2 = Thread(target=c.consumer)

t1.start()
t2.start()
