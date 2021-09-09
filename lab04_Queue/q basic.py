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

ip = input("Enter people : ")