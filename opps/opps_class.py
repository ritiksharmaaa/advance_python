
# example 2 
class myclass(object):
    def show(self):
        print('i am a methods ! ')

x = myclass()
x.show()

#exampe 3 
class mobile:
    def __init__(self, *args, **kwargs):
        self.model = 'RealMeX'
    def show_model(self):
        print(f"the model is { self.model}")

realme = mobile()
realme.model = 'proXṇ'
realme.show_model()

# example 4 

class mobile1:
    def __init__(self, *args, **kwargs):
        self.model = 'RealMeX'
    def show_model(self):
        price = 3000
        print(f"the model is { self.model} - and price is {price  }")

realme1 = mobile1()
realme1.show_model()


#example 5 


class mobile2:
    def __init__(self, m ):
        self.model = m 
    def show_model(self , p):
        price = p
        print(f"the model is { self.model} - and price is {price  }")

realme2 = mobile2('realme2')
realme2.show_model(6000)

realme22= mobile2('realme2')
realme22.show_model(3000)

# see each object have yhere own address
# print(id(realme2))
# print(id(realme22))




        
    

# ----------------------constructor----------------------

class Mobile:
    def __init__(self):
        print(" Mobile is constructor called ")

realme = Mobile() # at that time constructor can be called either other thing happen or not .

# or all method have in upper code are here also .


#-------------------------instance of variable type ----------------------
# check txt 

class Mobile:
    def __init__(self):
        self.model = 'reamleX'
    def show_model(self):
        print(self.model)
realme = Mobile()
print(realme.model)
realme.model = "realme_2" # change model in realme insaace not affect by other instance we check .
print(realme.model)

redmi = Mobile()
print(redmi.model) # heremodel is relmex notchaage because each instace have there own copies .


#-------------------------------------class variable / static variable --------------


class Car:
    discount = "50%"
    def __init__(self , p  ):
        self.price = p 
    @classmethod
    def is_discount(cls):
        print(cls.discount)
        

maruti = Car(3000) 
bike = Car(7000) 
truch = Car(3000) 

print(Car.discount) # getting class variable outside class
Car.discount = "100%" 
print(maruti.is_discount()) # getting clss variable inside class 
print(maruti.price) # getting clss variable inside class 

print(bike.discount) # getting class variable outside class 
print(bike.is_discount()) # getting clss variable inside class 
print(bike.price) # getting clss variable inside class 
