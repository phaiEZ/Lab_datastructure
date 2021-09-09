x = input("Enter Your List : ").split()
zero = True
for i in range (len(x)) :
    if (int(x[i]) != 0):
        zero = False
if(len(x) < 3):
    print("Array Input Length Must More Than 2")
elif(zero):
    print("[[0, 0, 0]]")
else:
    tempList =[]
    tempL=[]
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                if ((int(x[i]) + int(x[j]) + int(x[k]) == 0) and i < j < k ):
                    #print(str(x[i]) + " " + str(x[j]) + " " + str(x[k]))
                    tempL.append(int(x[i]))
                    tempL.append(int(x[j]))
                    tempL.append(int(x[k]))
                    #print(tempL)
                    tempList.append(str(tempL))
                    tempL.clear()
print(str(tempList).replace("'",""))
    