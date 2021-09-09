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
    
    def Show(self):
        x= ""
        for i in self.items:
            t = i + " "
            x += t
        return(x)

inp = input('Enter Input : ').split()
S = Stack()
temp = ""
count = 0
combo = 0
isCombo = False
for i in inp:
    S.push(i)

    if(temp == i):
        count += 1
    else:
        temp = i
        count = 1

    if(count == 3 ):
        S.pop()
        S.pop()
        S.pop()
        isCombo = True
        combo += 1
        count += 1
        temp = ""
while(isCombo):
    inp = S.Show().split()
    S = Stack()
    temp = ""
    count = 0
    isCombo = False
    for i in inp:
        S.push(i)

        if(temp == i):
            count += 1
        else:
            temp = i
            count = 1

        if(count == 3 ):
            S.pop()
            S.pop()
            S.pop()
            isCombo = True
            combo += 1
            count += 1
            temp = ""
if(S.size() == 0):
    print(0)
    print("Empty")
else:
    print(S.size())
    print(S.Show().replace(" ","")[::-1])
if(combo >= 2 ):
    print("Combo : "+ str(combo) + " ! ! !")

### Enter Your Code Here ###