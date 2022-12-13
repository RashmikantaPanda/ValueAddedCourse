mark1=int(input("Enter mark1 : "))
mark2=int(input("Enter mark2 : "))
mark3=int(input("Enter mark3 : "))
mark4=int(input("Enter mark4 : "))
mark5=int(input("Enter mark5 : "))

averageMark=(mark1+mark2+mark3+mark4+mark5)//5

print("Average mark : ",averageMark)

if averageMark>=90:
    grade="O"
elif averageMark>=80:
    grade="E"
elif averageMark>=70:
    grade="A"
elif averageMark>=60:
    grade="B"
elif averageMark>=50:
    grade="C"
else :
    grade="D"

print("Grade : ",grade)


