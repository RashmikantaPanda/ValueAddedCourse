class A:
    a=10
    def info(self):
        print(self.a)

class B(A):
    pass

b=B()
print(b.a)
b.info()

#MRO (Method Resolution Order
class A:
    a=10
    def info(self):
        print(self.a)
    def display(self):
        print("Display method of Class A")

class B(A):
    a=20
    def info(self):
       print(self.a)


b=B()
print(b.a)
b.info()
b.display()

print("----------------------")                   
class Student:
    def __init__(self,name,roll):
        #Instance variable
        self.name=name
        self.roll=roll

    def info(self):
        print(self.name, self.roll)

s=Student("Jyoti",200)
s.info()

