class Duck:
    def walk(self):
        print("thapak thapak thapak ....")
class horse:
    def walk(self):
        print(" horse walk thapak thapak thapak ....")

def myfunction(obj): # here we have obj no matter which obj have 
    obj.walk() # if they have required behaviour in object it will call 

d = Duck()
myfunction(d)

h = horse()
myfunction(h)

class cat:
    def talk(self):
        print(" cat walk ....")

c = cat()
# myfunction(c) # here we get error because myfunction does to matter what obj are came . it run when the obj have it behaviour function present . 

''' it is same as variable 

a = 12 

a type is int - because a assign with no - so a type depend on no ,

same as function is depend ob obj - obj int than function int type it just for learning purpose '''

# ---------------strong typing -----------
print("----------------------strong typing -------------------")

def function(obj):
    if hasattr(obj , "walk"):
        obj.walk()
    # calling based on / define function in duck function to handel all methods 
    if hasattr(obj , "talk"):
        obj.talk()
    # else:
    #     print(" obj has not method whichh you call ")
#d it intial upper code 
function(d)
function(c)

