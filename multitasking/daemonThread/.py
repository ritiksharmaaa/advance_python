from threading import Thread  , current_thread

def disp():
    print("DaemonThread")

t1 =Thread(target=disp)
t1.setDaemon(True)
print(t1.isDaemon()) # alos use t1.daemon this is property .
t1.start()

print(current_thread().getName()) # or name 

#check main thread is daemon or non 

ct = current_thread()
print(ct.name)
print(ct.daemon)

#-----------

# when main thread is non-daemo  so when you make t1 t2 is also non -deamon . 

# when we set t1 to daemon it return true 

# when you main thread became so you t1 t2also daemon that why wehave true as well false methods . 

# suppose t1 run functio in fuction it create t2 than t2 daemon have or not depend on parent daemon . is parent daemon chil also daemon . 
# and vice versa .