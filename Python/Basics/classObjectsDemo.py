class Person:
    name=""
    age=0

    def __init__(self,name,age):
        print("Object is created")
        self.name=name
        self.age=age

    def info(self):
        return f"{self.name} {self.age}"

    def __str__(self):
        return f"Name : {self.name} Age : {self.age}"



p=Person("Rashmi",20)
print(p.info())
print(p)