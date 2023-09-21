# when multi task are excutred at a time , then it is called multi-tasking for this purpose we need more then on  thread and when we use more than one thread it is called multi tasking . 


# tow task  using miti thread 

from threading import Thread 

class Hotel:
    def __init__(self , t ):
        # t is a table 
        self.t = t
    
    def food(self):
        for i in range(6):
            print(self.t , i )



h1= Hotel("Take order from table")
h2 =Hotel("Take order serve order")

t1 = Thread(target=h1.food )
t2 = Thread(target=h2.food )

t1.start()
t2.start()



# here one problem came it take order 215 but it serve first 24 , but 2 4 not give order so this condition called rece condition . 