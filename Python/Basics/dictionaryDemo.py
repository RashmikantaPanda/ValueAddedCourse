#Dictionary
#Word:meaning
d={1:"Rashmi",2:"Jyoti",3:"Rashmi"}
print(d)
s={}
print(type(s))


std={1:['c','c++'],2:['Python','Java','Django']}

for r,sub in std.items():
    print(f"Roll {r} knows ",end=" ")
    for s in sub:
        print(s,end=" ")
    print()