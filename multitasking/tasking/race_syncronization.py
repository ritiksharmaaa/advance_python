from threading import Thread  , current_thread , Lock
import time 

# class Flight:
#     def __init__(self , available_seat):
#         self.available_seat = available_seat
#     def reserver(self , need_seat):
#         print("Available seats are " , self.available_seat )
#         if (self.available_seat >= need_seat):
#             name = current_thread().name
#             print(f"{need_seat} seat is alloted for {name}")
#             self.available_seat -= need_seat 
#         else:
#             print("sorry ! all Seat has alloted !!")

# f = Flight(1)
# t1 = Thread(target=f.reserver , args=(1,) , name="rahul")
# t2 = Thread(target=f.reserver , args=(1,) , name="sonam")
# t1.start()
# t2.start()

#So we write a function just like that when one thread is working on a particular line of code another thread was not working on that particular code when the already a Thread working on that code. 

# Raise condition US situation that a carbon trade are acting in an unexpected sequence thus leading to unreliable output.

# - ---- solution -------

# This can be eliminated using thread synchronization 




# syncronization 

from threading import Thread  , current_thread 

class Flight:
    def __init__(self , available_seat):
        self.available_seat = available_seat
        self.i = Lock()
    def reserver(self , need_seat):
        self.i.acquire(blocking=True , timeout=-1) # this are scronization with lock 
        print("Available seats are " , self.available_seat )
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f"{need_seat} seat is alloted for {name}")
            self.available_seat -= need_seat 
            time.sleep(4)   # hereo timout so it gice acesse to another thread .
        else:
            print("sorry ! all Seat has alloted !!")
        self.i.release() # end of scrnoization with lock .

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

