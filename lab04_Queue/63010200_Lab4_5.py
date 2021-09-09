class Queue:

	def __init__(self):
		self.elements = []

	def enqueue(self, data, type = 0 ,mirorc = None):
		if(len(self.elements) >= 2):
			if((self.elements[-1] == self.elements[-2]) and (data == self.elements[-2])):
				#print("pop",data)
				if(type == 0):
					self.elements.pop()
					self.elements.pop()
					#print("ตู้ม")
					return(1)
				elif(type == 1 and (data == mirorc)):
					self.elements.pop()
					self.elements.pop()
					self.elements.append(mirorc)
					#print("ตู้มพิเศษ")
					return(2)
					#บวกการระเบิดแบบพิเศษ
				elif(type == 1 and (data != mirorc)):
					self.elements.append(mirorc)
					#print("แทรก")
					self.elements.append(data)
					return(3)

		self.elements.append(data)
		return(4)
		
	def dequeue(self):
		return self.elements.pop(0)

	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return len(self.elements) == 0

	def Print(self,x = 0):
		s = ""
		if(self.is_empty() and x == 0):
			s+= "ytpmE"
		else:
			for j in self.elements:
				s+= j
		return(s)

	
	def Show(self):
		return self.elements

ip,miror = input("Enter Input (Normal, Mirror) : ").split()
# print(ip)
# print(miror)


expo = 0
expomir = 0
interruptF = 0



mir = Queue()
nm = Queue()
temp = []
miror = miror[::-1]
for i in miror:
	#print(i)
	if (mir.enqueue(i) == 1):
		temp.append(i)
		expomir += 1
	#print(mir.Show())
temp.reverse()
#print(temp)
# count = 0
# print(len(temp))
for i in ip:
	# print(count)
	# print("len = ",len(temp))
	if(len(temp) > 0):
		tempo = nm.enqueue(i,1,temp[-1])
		#print(tempo)
		if(tempo != 4):
			#print("pop",temp[0])
			temp.pop()
		if(tempo == 1):
			expo+= 1
		elif(tempo == 2):
			interruptF += 1

		
	else:
		tempo = nm.enqueue(i)
		if(tempo == 1):
			expo+= 1
		
		#print(tempo)

	#print(mir.Show())
# print("NORMAL :")
# print(len(nm.Show()))
# print(nm.Print()[::-1])
print("NORMAL :")
print(len(nm.Show()))
print(nm.Print()[::-1])

print(expo,"Explosive(s) ! ! ! (NORMAL)")
if(interruptF != 0):
	print("Failed Interrupted",interruptF,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(len(mir.Show()))

if(len(mir.Show()) > 0):
	print(mir.Print()[::-1])
else:
	print(mir.Print())
print("(RORRIM) ! ! ! (s)evisolpxE",expomir)