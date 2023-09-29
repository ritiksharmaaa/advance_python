# Pickling in python 

import pickle  , pick 

n = int(input("Enter Number of student : "))
with open("pickling.dat" , "wb") as f :
    for i in range (n):
        name = input("Enter User name ")
        roll = int(input(" Enter user roll number : "))
        address = input("Enter your Address")
        stu1 = pick.Student(name  ,roll  , address )
        pickle.dump(stu1 , f) # f is file anme  


print('pickling done ')







 

# here data creation happen : - 

# # comment for making user friendly 
# with open("pickling.dat" , "wb") as f :
#     stu1 = pick.Student("ritik" , 2234 , "nand gram ghaziabad ")
#     stu2 = pick.Student("shalini " , 2234 , "nand gram ghaziabad ") # adding extra data in file 
#     pickle.dump(stu1 , f) # f is file anme 
#     pickle.dump(stu2 , f) # f is file anme 
#     print('pickling done ')
# # the data save in file is not readable becuse it not write data as normal it like litbit hasing and manymore 



