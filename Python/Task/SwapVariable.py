#Swap two variable
a=int(input("Enter a nubmer "))
b=int(input("Enter a nubmer "))

print("-----Before Swapping------")
print("Value of a=",a)
print("Value of b=",b)

print("-----After Swapping-----")
#Swap 
a=a+b
b=a-b
a=a-b
print("value of a =",a)
print("value of b = ",b)
