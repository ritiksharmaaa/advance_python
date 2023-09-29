
import pickle, pick 


#reading object from file 

with open("pickling.dat" , "rb") as f :
    while True :
        try:
            obj = pickle.load(f)
            obj.disp() # it give error but give because of while loop so we have to handel it . 
        except EOFError:
            print("done")
            break 
