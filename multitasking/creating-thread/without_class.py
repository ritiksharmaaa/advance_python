# creating thread without class 
from threading import Thread , current_thread 
def disp(a , b):
    print("iam  child thread threading " , a , b)

t = Thread(target=disp , args=(10 , 20 )) # here tubple single when you put ,  or / this is excute via main thread 
# t.start() # or hera the both main and new are seprate . 
# print(t.start())

# for i in range(10):
#     t=Thread(target=disp , args=(12 , 10))
#     t.start()



# here child thread wotk inside the main thread , but only start one they start our child threaad , they both are alag ho jayege . 


def d():
    for i in range(5):
        print(" child thread ")
b = Thread(target=d)
b.start() # start thread 
for i in range(5):
    print("mainthread")

    # otput came chil dhreat main thread un pattern because they both are running parlal . 


# ------------------------------- threading with getnad set and property name ------------ 

# please check latest doc to access it name . 


def fun():
    print(" child thread object ---------------------" , current_thread().name)
    print("++++++++++++++++++++")
    current_thread().name = "flying"
    print(" child thread object ---------------------" , current_thread().name)


n = Thread(target= fun )
n.start()


print("main thread------------------------------ " , current_thread().name)

# here output are not get in proper way because here programe run simitniously so ine is just start suddenly second give ther own resulr =t .





    
#  hthread with constructor .

class Construct_thread(Thread):
    def __init__(self , a):
        super().__init__(self)
        self.a = a 
    def run(self):
        pritn("constrctor thread run methods ")

m = Construct_thread(a)
m.start()