# we make two thread one for red and green and second for walk and stop . 

from threading import Thread , Event 
from time import sleep


def light_switch():
    sleep(3) # not show anything 
    e.set()
    print("Green Light One ")
    sleep(.5)
    print("Red Light On ")
    e.clear()



def traffic():
    e.wait()
    while e.is_set():
        print("You can Go ......................")
    print(" stop .............. ")

e = Event()


t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()
t2.start()


