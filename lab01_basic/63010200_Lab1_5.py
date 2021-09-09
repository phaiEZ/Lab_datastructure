x = int(input("Enter Input : "))
for i in range(x+2):
    print("."*((x+1)-i),end="")
    print("#"*(i+1),end="")

    if((i == 0 )or( i == (x+1))):
        print("+"*(x+2))
    else:
        print("+",end="")
        print("#"*x,end="")
        print("+")

for i in range(x+2):
    if((i == 0 )or( i == (x+1))):
        print("#"*(x+2),end="")
    else:
        print("#",end="")
        print("+"*x,end="")
        print("#",end="")
    print("+"*((x+2)-i),end="")
    print("."*(i))