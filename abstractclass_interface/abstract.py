from abc import ABC , abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass # this function define in child class 
    def show(self):
        print("i am concrete methods ! ")
    
# this farher class you not nake instance object and call it . 

# my = Father() give erro becuse you cant do ths . 

class Child(Father):
    def disp(self):
        print("child class ")
        print("defining abstract class ")


c = Child()
c.disp()
c.show()


    