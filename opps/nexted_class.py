# nested class 

class Army:                 # outer class 
    def __init__(self):
       self.name = "rahul" 
       self.gn = self.Gun()  # inner class here---- gn is instace of inner  class so we use it method and 
    def show(self):
      print(self.name)
   
    # now making actual class 
    class Gun :
        def __init__(self):
            self.name = "ak47"
            self.capacity = "75 round"
            self.length = '34.3 inch'
        def desp(self):
            print("gun name : - " , self.name )
            print('gun fire round : - ' , self.capacity)
            print('gun length : - ' , self.length)
    


a = Army() # initial outer class 
a.show() # using outer insatnce function 

a.gn.desp()  # here class instance var is actual instance of inner class 

# here we intialize first define furthure .
b = a.gn # now we can perform direct;y by this b ,it easy 
b.desp()
print(b.name ,"-----------------------") 

