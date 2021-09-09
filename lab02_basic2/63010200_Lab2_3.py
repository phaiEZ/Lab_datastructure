def Range(a ,b=-1,c=1):
    temp = ""
    if (b == -1):
        i = 0
        while(i < a):
            temp += str(round(float(i),3))+", "
            i += 1
    else:
        i = a
        while(i < b):
            temp += str(round(float(i),3))+", "
            i += c
    return("(" +temp[:len(temp)-2]+")")



print("*** New Range ***")
x = input("Enter Input : ").split()
if (len(x) == 1):
    print(Range(float(x[0])))
elif (len(x) == 2):
    print(Range(float(x[0]),float(x[1])))
elif (len(x) == 3):
    print(Range(float(x[0]),float(x[1]),float(x[2])))