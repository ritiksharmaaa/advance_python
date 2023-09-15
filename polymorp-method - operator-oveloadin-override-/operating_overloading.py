#If any operator perform additional action other than what is meant for it is called operator overloading suppose we have so many operator like plus minus divide and multiplication many more these are called center operator.

print(10+3) # here whathappent 

# here when you run it run this function 

# int.__init__(self , other) # So you have to not run these functions each time when you have to do spontaneity multiplication add subtraction and many calculation so here the short form called pluswe can use directly to add.

print(int.__add__(10 , 12)) # this for int val concate   here int ans str is function which take paremater for perfoming task  make a nick name + so we use + ranther than this methods . 
print(str.__add__('madhu', 'sharma')) # this use for adding to string .

# we have so methods for that 

# __add__(self , other)   #these are called magic methods or alos dunder .
# __sub__(self , other)
# __mul__(self , other)

# so when ever we use + method to add it calll __add__ method . 

# when you add int and str it gave error because + (nick name ) has no any function to add two int and str 

# so we can overloding this class and function to do that . 

class a :
    def __init__(self , x ):
        self.x = x 
class p:
    def __init__(self , x):
        self.x = x 

# note . when we use var to add a = 4 , b = 5 (-------print(a+b)) here a has autodect that this is a int than int.__add__(self.other)  run 
# so there str. ave __add__mmethods to ad object .

# what happen we have class a = clas(val)   here a is not detech which type they have so when you add by + so class var is not int and not var function  like str pr int class . here class name is function . a = class here a hase function like str and int have so when you add this to instance . it fin add method +(__add__(self, other ))

# but in  class instancevar donrt have __add__ method so it give fail . 

# but can do operator overloading . 

# ex
print('iam runing ')
a = a(100) # p called a instance obj 
p = p(100)

# print(a+p) # here a is not int or not str so __addFiction how it work because __str method is not define fo class instanceo bject  var . 

# give error upsopted operands for + : a and p 

# so we have to make that function for instance var in class methods . 



# new class
class A :
    def __init__(self , x ):
        self.x = x 
    def __add__(self , other):
        print(self.x , other.x ,'i am runing before additione ')
        return self.x + other.x
class P :
    def __init__(self , x):
        self.x = x 

A = A(200)
P = P(200)
print(A+P)


# bacically we do add function in instance object . 

# means when 12+14 happen here int.__add__(12 , 14) are passed in this int class methods . so that thing happen traditionaly . 
# this for str str.__add__(self , other )
# obj = for obj there is no class male like obj.__add__(self , other ) # we made it manaualyy . 




