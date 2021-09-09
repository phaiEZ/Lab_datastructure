def odd_list(x):
    for i in range(len(x)):
        if (int(x[i]) % 2) == 0:
            x[i] = "j"
    while("j" in x):
        x.remove("j")
print(" ***Function Odd List***")
x = input("Enter list numbers : ").split()
print("Input list :  "+ str(x).replace("'",""))
odd_list(x)
print("Output list :  "+ str(x).replace("'",""))