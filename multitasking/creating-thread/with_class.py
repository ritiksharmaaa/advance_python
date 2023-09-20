# thread with class 

from threading import Thread  , current_thread

class ChildThread(Thread):
    # method to see how join work 
    def run(self):
        for i in range(5):
            print("child thread ")

    # def run(self):  # this method is writen in thrread class we overide to make own class .
    #     print(" run methods ")

    
# ?run ---------------

t = ChildThread()
print(t.name)
t.start() # when it call this method call run methods .
# print(current_thread().name) # main thread 

# join method

# ?join 


# this line code done for do join 

t.join() # run when we wna to run thrad in paticular patter or first give preferrence . 

for i in range(5):
    print("main thread")

    # we know when thread create by main thread it seprate after created .

# """ if we run code this excuted parralel but no patter follow . we want to first excute chil thread than  any other thread run ex main thread so we join  



# ----------------- with constructor ----------

print("----------------------------------------------------------------------------------")



class Construct_thread(Thread):
    def __init__(self , a):
        Thread.__init__(self)
        self.a = a
        print(" initailise constructor thread ! !  " , self.a)
        print(current_thread().name)
    def run(self):
        print("constrctor thread run methods ")
        print(current_thread().name)

m = Construct_thread(12)
m.start()
