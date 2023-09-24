# make a example project : - 

from threading import Thread , current_thread 
from time import sleep

def Teacher():
    for i in range (1,11):
        print(" Teaching session " , i )
        sleep(1)

t1 = Thread(target=Teacher) # this thread is non daemon because his main thread is non daemon . 

# change for problem solution 

t1.setDaemon(True)  # this help to main thread whichin non-demon - if non dameno task complete thnat daemon thread stop and terminate all call ()

t1.start()
sleep(6)
#t1.join() if want to excute full session 
print(" exam finished " , current_thread().name) 

#problem why we use daemon thread 

# output after run 

''' Teaching session  1
 Teaching session  2
 Teaching session  3
 Teaching session  4
 Teaching session  5
 Teaching session  6
 exam finished  MainThread    # here  exam finish but session chal raha hai .
 Teaching session  7
 Teaching session  8
 Teaching session  9
 Teaching session  10'''


# ex -  bgmi 

# max is hero  and his villian has so much chamche if max kill main villan what chamce do .
