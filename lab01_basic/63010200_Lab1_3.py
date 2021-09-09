print("*** Reading E-Book ***")
x,y = input("Text , Highlight : ").split(',')
for i in range(len(x)) :
    if x[i] == y :
        print('['+y+']',end='')
    else :
        print(x[i],end='')