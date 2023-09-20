# here we daint use uction and child class only use of thread by creating that function to a thread /.
from threading import * 



class myThread():
     def disp(self , a , b ):
         print(a , b )


mthread = myThread()

thread_object = Thread(target= myThread.disp , args=(10 , 12 ))

thread_object.start()

print(current_thread)