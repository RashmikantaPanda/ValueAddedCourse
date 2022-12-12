a=int(input("Enter first numeber : "))
b=int(input("Enter second number : "))
op=input("Enter  operator")
match(op):
    case '+':
        print(f"Sum ={a+b}")
    case '-':
        print(f"Difference ={a-b}")
    case _:
        print("Nothing")