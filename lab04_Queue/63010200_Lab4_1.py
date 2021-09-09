class Queue:
	def __init__(self):
		self.elements = []

	def enqueue(self, data):
		if data != None :
			self.elements.append(data)
			return data

	def dequeue(self):
		if(not self.is_empty()):
			x = self.elements.pop(0)
			print(x,end=" <- ")
			return x


	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return (len(self.elements) == 0)

	def Print(self,x = 0):
		if(self.is_empty() and x == 0):
			print("Empty")
		elif(self.is_empty() and x == 1):
			print("Empty",end = "")
		else:
			if (x == 1):
				for j in self.elements:
					if(j != self.elements[-1]):
						print(j,end=", ")
					else:
						print(j,end="")
			else:
				for j in self.elements:
					if(j != self.elements[-1]):
						print(j,end=", ")
					else:
						print(j)



x = input("Enter Input : ").split(",")
q = Queue()
t = Queue()
for i in x :
	if(i[0] == "E"):
		q.enqueue(i[2])
		q.Print()
	elif(i[0] == "D"):
		t.enqueue(q.dequeue())
		q.Print()

t.Print(1)
print(" : ",end = "")
q.Print(1)