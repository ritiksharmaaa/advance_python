# lst = []
# # for i in range(6):
# #     name = input(" enter your name !! ")
# #     lst.append(name)

# for i in lst:
#     print(i) # here is no use of file we store some name after running data close if we remove append methods 
# # nothing will print because no dat save . in list it just temporary holding data .


# f = open('student.pdf' , mode='w')
# f.write(" i am student ")

# f.close()



# ---------------- check all that mode ----------

f = open('student.pdf' , mode='w')
f.write(" i am student2 \n ")
f.write(" i am student3 \n ")
f.write(" i am student1 \n ")
f.close()
print(" writing sucessfully !!")
f = open('student.pdf' , mode='r')
data = f.read()# here data decode 
print(data)
f.close()

f = open('student.pdf' , mode='rb')
data = f.read()# here data does nt decode . 
print(data)
f.close()

# -----------------------------------------------------------opening a file ----------------- check .txt file 



 # see uper object also do writen 