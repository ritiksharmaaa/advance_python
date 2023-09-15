# hierachial class

class Father:
    def show(self):
        print("parent")

class child_1(Father):
    def show1(self):
        print("parent child 1 ")

class child_2(Father):
    def show2(self):
        print("parent child 2 ")
s1 = child_1()
s1.show()
s2 = child_2()
s2.show()


# _______________ same as use constructor as weprevious learn ------------------


