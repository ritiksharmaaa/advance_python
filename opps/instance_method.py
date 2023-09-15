# #accesor /getter or muttator/setter


# this is instance methods : --


class mobile:
    def __init__(self):
        self.model = 'realmeX'  # instance variable 
    def show_model(self  , p ):  # instance methods 
        self.price = p 
        print('model:', self.model , 'price :' , self.price)

realme = mobile()  # object instance 
realme.show_model(1000)

redmi = mobile() # when you initialize it it can pass instance address to self 
redmi.show_model(6000)



#----------------------------------Accessormethods /gette  --------------------------------------

# These method is used to access or read data of a variable the method do not modify the data in the variables this is also called as getter method

#(mean) -This method is made just for read but we have also update or change but this method is not made for update or change this method is only made for read the variable.

#In my opinion the accessor or ghetto method this is just a normal insane method but we are insane method we getting the parameter and change it and return something else but in this method what we are doing we are makinga function which directly gives us that variable we don't have to first make the instance when instance dot variable name then we getting the thing this is so difficult and not good so that is why we are making a accessor method to just directly getting the variable by calling it.

class Mobile:
    def __init__(self):
        self.model = "realmeX"
    #making getter / accesor methods . write as it because convention way 
    def get_model(self):
        return self.model 

    def set_value(self):
        self.model = "redmi"

redmi = Mobile()
get = redmi.get_model() # that functionality we need to acces variabe fastly 
redmi.set_value() # setter method called .
met = redmi.get_model()
print(met)
print(get)



#----------------------------------------------------mutator/setter mrthods --------------------------------------

#The method is used to access or read and modify data of the variable this method modify the data is the variable this is also called Assetter method.

#ex - set_value()

# code written in upper code ^^^^