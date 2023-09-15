# class and stati methods 

# in variable class varibale and static variable is same but in method diffrent .

class Mobile:
    ps = "yes"

    @classmethod
    def show_model(cls , r ):
        cls.rate = r  # adding extra class variable via this parameter 
        print(cls.ps , cls.rate)

#calling it 

realme = Mobile()
realme.show_model(10000)

# -------------------------------------static methods --------------

# without parameter 

class monkey:
    jp = "banana"
    @staticmethod
    def jump_outside():
        print("monkey jump ... ")

    # without parameter 
    @staticmethod
    def jump(b , m ):
        b = b 
        m = m
        print(b ,"=" , m)


#calling without parameter 

m = monkey()
m.jump_outside()
m.jump("ekdum" , "jhatse ")
