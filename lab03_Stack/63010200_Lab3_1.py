class Stack:
    def __init__(self):
	    self.items = []
    def isEmpty(self):
        return self.items == []
	
    def push(self, item):
	    self.items.append(item)
	
    def pop(self):
	    return self.items.pop()
	
    def peek(self):
	    return self.items[0]

    def size(self):
	    return len(self.items)
    def Print(self):
        print("Value in Stack = ",end="")
        for i in self.items :
            print(i,end=" ")
        
x = input("Enter Input : ").split(',')
S = Stack()
for i in range(len(x)):
    x[i] = x[i].split()
for i in range(len(x)):
    if(x[i][0] == "A"):
        S.push(x[i][1])
        print("Add = "+ str(x[i][1]) + " and Size = "+ str(S.size()))
    elif(x[i][0] == "P"):
        if(S.size() <= 0 ):
            print(-1)
        else:   
            print("Pop = "+ str(S.pop()) + " and Index = "+ str(S.size()))
if(S.isEmpty()):
    print("Value in Stack = Empty")
else:    
    S.Print()