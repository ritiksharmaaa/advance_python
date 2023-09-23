from threading import Thread  , current_thread , Lock , Semaphore , BoundedSemaphore 
import time 





# syncronization  with semophore . and bounded semaphore 

from threading import Thread  , current_thread 

class Flight:
    def __init__(self , available_seat):
        self.available_seat = available_seat
        # self.i = Semaphore(2)
        self.i = BoundedSemaphore(3)
        print(self.i)
    def reserver(self , need_seat):
        self.i.acquire(blocking=True , timeout=-1) # this are scronization with lock 
        print(self.i.value ) # give yiu count how many time call and what value have .
        print("Available seats are " , self.available_seat )
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f"{need_seat} seat is alloted for {name}")
            self.available_seat -= need_seat 
            time.sleep(4)   # hereo timout so it gice acesse to another thread .
        else:
            print("sorry ! all Seat has alloted !!")
        # self.i.release()
        # self.i.release()
        # self.i.release()
        # self.i.release()# multiple time reale in semaphore 
        self.i.release()

f = Flight(2)
t1 = Thread(target=f.reserver , args=(1,) , name="rahul")
t3 = Thread(target=f.reserver , args=(1,) , name="mohan")
t2 = Thread(target=f.reserver , args=(1,) , name="sonam")
t1.start()
t2.start()
t3.start()
print("main Thread ") # this run un between any one . so join to run serialy .
t1.join()
t2.join()
t3.join()




# reentrate lock ()Rlocck syncronization . 


# inside acuare or realse one problem is called deadcall 


