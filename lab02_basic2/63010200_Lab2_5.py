class funString():
    stri =""
    def __init__(self,stri):
        self.stri = stri 
    def size(self) :
        x = self.stri

        return(len(self.stri))

    def changeSize(self):
        x = self.stri
        temp = ""
        for i in x:
            if (ord(i) >= 97):
                temp += chr(ord(i) - 32)
            elif(ord(i) >= 65):
                temp += chr(ord(i) + 32)
        return(temp)

    def reverse(self):
        x = self.stri
        temp = ""
        for i in range(len(x)):
            temp += x[(len(x)-1)-i]
        return(temp)

    def deleteSame(self):
        x = self.stri
        temp = ""
        temp += x[0]
        for i in range(len(x)-1) :
            if(not (x[i+1] in temp)):
                temp += x[i+1]
        return(temp)



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())