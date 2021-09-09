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
        x =""
        for i in self.items :
            x += i
        return(x)



open = set('[{(')
close = set(')}]')
match = set([('(',')') , ('{','}') , ('[',']')])
ischeck = True
ans = Stack()
x = input("Enter expresion : ")
for i in x:
    #print(i)
    if i in open:
        ans.push(i)
    elif i in close :
        if(ans.isEmpty()):
            print(x +" close paren excess")
            ischeck = False
            break
        elif((ans.pop(),i) not in match ):
            ischeck = False
            print(x +" Unmatch open-close")
            break
    
if(not ans.isEmpty() and ischeck):
    print(x +" open paren excess   " + str(ans.size()) + " : " + str(ans.Show()))
elif(ans.isEmpty() and ischeck):
    print(x +" MATCH")
