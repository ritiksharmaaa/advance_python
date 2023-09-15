class myclass:
    def sum(self , a):
        print("ist sum method" , a )
    def sum(self):
        print("iind sum method calling .............")


# problem your ist method not work / second method call always ...  so it show error 

# obj = myclass()
# obj.sum()
# obj.sum(4)

class mycl:
    def sum(self , a , b , c):
        s = a + b + c 
        return s 

''' here what happen when we pass only two paramete than how it can handel it 

we have to pass default val in parameter . 
'''


class mycl1:
    def sum(self , a=None , b=None , c=None):
        if a!=None and b!=None and c!=None:
            s = a + b + c 
            return s 
        else:
            print('sum ho gya ! ')


b = mycl1()
print(b.sum(12 , 23, 45))
print(b.sum())