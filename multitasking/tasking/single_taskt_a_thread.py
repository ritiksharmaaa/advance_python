# when multiple task are excuted by a thread one by one , then it called single tasking .

# writing examination 
''' question 1 , question 2 , question 3 
'''
from threading import Thread
from time import sleep 

class Myclass:
    def solve_question(self):
        self.q1()

        self.q2()
        self.q3()
    def q1(self):
        print(" quetion one solved !!")
        sleep(3)
    def q2(self):
        print(" quetion two  solved !!")
        sleep(3)
    def q3(self):
        print(" quetion three solved !!")
        sleep(3)

    

mye = Myclass()
t = Thread(target=mye.solve_question)
t.start()