class father:
    money = 1000

    def show(self):
        print("parent class instance methods")
    @classmethod
    def showmoney(cls):
        print("class methods of parent classs" , cls.money)

    @staticmethod 
    def stats():
        print("static method of fathr class")

class son(father):
    def disp(self):
        print("instace methos of son class ")

# s = son()
# s.disp()
# s.showmoney() # this is call from parent class 
# s.show()
# s.stats()

# ----------------------------- with constructor -----------


class Mother:
    def __init__(self):
        self.money = 1000 
        print("father class constructor")

    def show(self):
        print("father instance method .. ")
class Son(Mother):
    def disp(self):
        print("instance method of son class " , self.money)



# this work better when you dont have child constructor . 
# s = Son()
# print(s.disp())



# -------------------constructor overiding -------------------

# mean child class overide paren constructor 

class mom:
    def __init__(self , m):
        self.money = m
        # self.money = 1000
        print(" parent constuctor !")
    def show(self):
        print("parent instance methods ")

class beta(mom):
    def __init__(self , r):
        self.money = r 
        # self.money = 5000
        self.car = "BMW"
    def disp(self):
        # print("child instance methods ! " , self.money)
        print("child instance methods ! " )
# m = mom(1200)
# b = beta(2000)
# # print(b.money) this not wotrk beacuse we make own constructor in the class .
# b.disp()
# print(b.money)
# print(b.car)
# b.show() # calling parent class instance methods . 


# -----------------------------------super method or call parent cunstructor --------------





class Mom:
    def __init__(self , m=0):
        self.money = m
        # self.money = 1000
        print(" parent constuctor !")
    def show(self):
        print("parent instance methods ")

class Beta(Mom):
    def __init__(self , r=0):
        super().__init__() # calling upper class constructor 
        self.money = r 
        # self.money = 5000
        self.car = "BMW"
        print("son class construnctor ")
    def disp(self):
        # print("child instance methods ! " , self.money)
        print("child instance methods ! " )

B = Beta(3000)