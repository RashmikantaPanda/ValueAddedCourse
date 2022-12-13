#If the number is divisible by 3 print "Fizz" . If the number is divisible by 5 print "Buzz".
# If the number is divisible by both 3 and 5 print "FizzBuzz"

number=int(input("Enter a number : "))

if number%3==0 and number%5==0:
    print("FizzBuzz")
elif number%5==0:
    print("Buzz")
elif number%3==0:
    print("Fizz")
else:
    print("Number is : ",number)