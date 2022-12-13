#Write a python program to accept two integer numbers and perform all arithmatic operations 
# including exponent and floor operation

a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
op=input("Enter the operator : ")
res=0
match(op):
    case '+':
        res=a+b
    case '-':
        res=a-b
    case '*':
        res=a*b
    case '//':
        res=a//b
    case '/':
        res=a/b
    case '%':
        res=a%b
    case '**':
        res=a**b


print(f"{a} {op} {b} = {res}")