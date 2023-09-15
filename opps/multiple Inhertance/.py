# multiple inheritance 

class Father :
    def showF(self):
        print("father")

class Mother :
    def showM(self):
        print("Mother")

class son(Father ,Mother): # here postion also matter father first so fatehr constructor run first it mother vice versa 
    def showS(self):
        print(" son ")

s = son()
s.showF()
s.showM()


# Suppose we have construction in watch mother and father but when we call super method in sunny then when we initializing only father constructor is run this isa big problem to solve this problem what we do we have to define or call super method in each constructor in father it mother in son each each constructor have to be called super method which init function.

