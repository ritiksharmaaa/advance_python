# multilevel inheritance 


# class father :
#     def ShowF(self):
#         print("father function print ...")

# class son(father):
#     def showS(self):
#         print(" son function class ")
# class grandson(son):
#     def showG(self):
#         print("grandson also running function ....")


# g = grandson()
# g.showG()
# g.showS()
# g.ShowF()


# -----------------------------------with constructor ----------------

class father :
    def __init__(self):
        print("parent consrtuct ...........")
    def ShowF(self):
        
        print("father function print ...")

class son(father):
    def __init__(self):
        super().__init__()
        print("son  consrtuct ...........")
    def showS(self):
        print(" son function class ")
class grandson(son):
    def __init__(self):
        super().__init__()
        print("grandson consrtuct ...........")
    def showG(self):
        print("grandson also running function ....")

# now which constructor call when we initialize grandson

g = grandson() # here only grandson constructor run 
# for more run supper meyhods .

#calling all constructor using super 



