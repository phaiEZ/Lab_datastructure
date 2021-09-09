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
	def Show(self):
		return self.elements


x = input("Enter people : ")
qmain = Queue()
q1 = Queue()
q2 = Queue()
for i in x:
	qmain.enqueue(i)
m1 = 0
m2 = 0
i = 1
while(not qmain.is_empty()):
	print(i,end=" ")
	if(m1 == 3):
		q1.dequeue()
		m1 = 0
	if(m2 == 2):
		q2.dequeue()
		m2 = 0
	if(len(q1.Show()) < 5 ):
		q1.enqueue(qmain.dequeue())
	elif(len(q2.Show()) < 5):
		q2.enqueue(qmain.dequeue())
	else:
		print("full")

	print(qmain.Show(),end=" ")
	print(q1.Show(),end=" ")
	print(q2.Show())

	if(not q1.is_empty()):
		m1 += 1
	if(not q2.is_empty()):
		m2 += 1
	i += 1