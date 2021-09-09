class Stack:
    def __init__(self):
        self.top = -1
        self.temp = []
        self.ans = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
     
    def isEmpty(self):
        return True if self.top == -1 else False
     
    def peek(self):
        return self.temp[-1]
     
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.temp.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.temp.append(op)
 
    def isOperand(self, ch):
        return ch.isalpha()
 
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except :
            return False
             
    def infixToPostfix(self, exp):
         
        for i in exp:
            if self.isOperand(i):
                self.ans.append(i)
              
            elif i  == '(':
                self.push(i)
 
            elif i == ')':
                while( (not self.isEmpty()) and
                                self.peek() != '('):
                    a = self.pop()
                    self.ans.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.ans.append(self.pop())
                self.push(i)
 
        while not self.isEmpty():
            self.ans.append(self.pop())
 
        print ("".join(self.ans))

print(" ***Infix to Postfix***")
ip = input("Enter Infix expression : ")
obj = Stack()
print("PostFix : ")
obj.infixToPostfix(ip)