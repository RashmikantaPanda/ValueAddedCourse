#Greater among two number
print("Greater among two number")
a=int(input("Enter first number :"))
b=int(input("Enter first number :"))
if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

#Greatest among three Numbers
print("Greatest among three Numbers")
a=int(input("Enter first number :"))
b=int(input("Enter first number :"))
c=int(input("Enter first number :"))

if a>b and a>c:
    print(f"{a} is greater")
elif b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")