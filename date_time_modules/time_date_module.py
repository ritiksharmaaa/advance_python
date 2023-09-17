from time import time , ctime , localtime 

from datetime import datetime 
epoch = time() 
print(epoch) # 1694942397.5997906

ct = ctime(epoch)
print(ct)

stobj = localtime()
print(stobj) # return lot of attribute use to get your time . 
print(stobj.tm_year , end="/") # give 2023 year .  here end is use a span print all dat in single line .
print(stobj.tm_mon , end="/") # give 2023 year . 
print(stobj.tm_mday) # give 2023 year . 



# --------------datetime module --------------
print(" date time modules . ")
dt = datetime(year=2019 , month=4 , day=12)
e = datetime(2017 , 3 , 13)
print(dt)
print(e)

# you acces by datetime.year , month dsay and many more .

# date time class methods . 

# some methods check in txt file 



