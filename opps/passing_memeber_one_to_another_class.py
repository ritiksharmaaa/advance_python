class student:
    def __init__( self , p , q ):
        self.p = p 
        self.q = q 
    def get_data(self):
        print(self.q)
        print(self.p)

#init and function nedd to send to other class not inhertance 

class user:
    @staticmethod
    def show_in(stu):
        print( "this function we get ..........  -- " ,stu )
        print(stu.p) #calling instance variable 
        print(stu.q)
        stu.get_data() # caling instance upper class funcrtion 

# main function see hear

m = student("raju" , "manju")
# not calling because we dont need it 

stu = user()
stu.show_in(m)

