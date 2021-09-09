class Stack:
    def __init__(self ):
	    self.items = []

    def isEmpty(self):
        return self.items == []
	
    def push(self, item):
        if(item != -1):
	        self.items.append(item)
	
    def pop(self):
        if(len(self.items) > 0):
	        return self.items.pop()
        else:
            return -1
	
    def Clear(self):
	    self.items = []


    def peek(self):
	    return self.items[0]

    def size(self):
	    return len(self.items)
    
    def Show(self):
        # x =""
        # for i in self.items :
        #     x += i
        #     x +=""
        return(self.items)
def getHigh(x):
    if((int(x)%2 == 0)):
        return int(x) - 1
    elif((int(x)%2 == 1)):
        return int(x) +2

def throwB():
    for i in range (temp.size()):
        x = temp.pop()
        main.push(x)
    # print("throw")

ip  = input("Enter Input : ").split(",")
main = Stack()
temp = Stack()
tempn = 0
nexttree = 0
nowtree = 0
drunk = False
for i in ip :
    if(i[0] == "A"):
        main.push(int(i[2:]))
        # print("found num = " + str(i[2]))
    elif(i[0] == "B" ):
        if(not(main.isEmpty())):
            # print("B")
            # print("main = ",end="")
            # print(main.Show())
            count = 1
            tempn = main.pop()
            # print("pop =",end ="")
            # print(tempn)
            nowtree = tempn
            if(drunk == True):
                temp.push(getHigh(int(tempn)))
            else:
                temp.push(tempn)
            while(1):
                tempn = main.pop()
                nexttree = tempn
                if(drunk == True):
                    temp.push(getHigh(int(tempn)))
                else:
                    temp.push(tempn)
                
                if(drunk == False):
                    if(int(nowtree) < int(nexttree) ):
                        # print("comp" ,end= " now:")
                        # print(int(nowtree))
                        # print("next:" ,end= " ")
                        # print(int(nexttree))
                        nowtree = nexttree
                        count += 1               
                else:
                    # print("comp" ,end= " now:")
                    # print(getHigh(int(nowtree)))
                    # print("next:" ,end= " ")
                    # print(getHigh(int(nexttree)))
                    if(getHigh(int(nowtree)) < getHigh(int(nexttree)) ):
                        
                        nowtree = nexttree
                        count += 1

                if(main.size() == 0):
                    break
            print(count)
            drunk = False
            throwB()
        else:
            print(0)

    elif(i[0] == "S" ):
        drunk = True


# print("temp = ",end="")
# print(temp.Show())
# throwB()
# print("main = ",end="")
# print(main.Show())

