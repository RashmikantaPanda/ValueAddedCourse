first=int(input("Enter the starting value : "))
end=int(input("Enter the ending value : "))

for i in range(first,end+1,1):
    if i%2!=0:
        print(i,end=" ")