class Queue:

	def __init__(self):
		self.elements = []

	def enqueue(self, data):
		self.elements.append(data)
		return data

	def dequeue(self):
		return self.elements.pop(0)

	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return len(self.elements) == 0

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
	def Show(self):
		return self.elements

q = Queue()
ip1,ip2 = input("Enter Input : ").split("/")
temp = str(ip1).split()
for i in temp:
	q.enqueue(i)
	#print(i)
# q.Print()
temp = str(ip2).split(",")	
for i in temp:
	if(i[0] == "D"):
		#print("DEQ",q.dequeue())
		q.dequeue()
	elif(i[0] == "E"):
		q.enqueue(i[2:])
		#print("EQ",q.enqueue(i[2]))
check = []

# q.Print()
Duplicate = False
while(not q.is_empty()):
	x = q.dequeue()
	if x in check :
		Duplicate = True
		break
	check.append(x)
if(Duplicate):
	print("Duplicate")
else:
	print("NO Duplicate")