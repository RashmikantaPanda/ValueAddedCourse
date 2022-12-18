try:
    a=int(input("Enter first number : "))
    b=int(input("Enter second number :"))
    c=a/b
    print("Result : ",c)
except ZeroDivisionError:
    print("Second number can not be zero")
except ValueError as ve:
    print("Enter a valid number")
except Exception as ex:
    print(ex)
finally:
    print("Finally block is executed")