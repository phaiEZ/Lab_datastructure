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
		stemp = ""
		if(self.is_empty() and x == 0):
			stemp += "Empty"
		elif(self.is_empty() and x == 1):
			stemp += "Empty"
		else:
			if (x == 1):
				for j in self.elements:
					if(j != self.elements[-1]):
						stemp += str(j)
						stemp += (", ")
					else:
						stemp += str(j)
			else:
				for j in self.elements:
					if(j != self.elements[-1]):
						stemp += str(j)
						stemp += (", ")
					else:
						stemp += str(j)
		return(stemp)
	def Show(self):
		return self.elements
me = Queue()
gf = Queue()
ip = input("Enter Input : ").split(",")
for i in ip:
	temp = i.split()
	me.enqueue(temp[0])
	gf.enqueue(temp[1])

print("My   Queue = ",end = "")
print(me.Print())
print("Your Queue = ",end = "")
print(gf.Print())

ansme = "My   Activity:Location = "
ansgf = "Your Activity:Location = "
score = 0
activity = ["Eat","Game","Learn","Movie"]
place = ["Res.","ClassR.","SuperM.","Home"]
while(not me.is_empty()):
	temp_me = me.dequeue()
	temp_gf = gf.dequeue()
	if(temp_me[0] == temp_gf[0] and temp_me[2] == temp_gf[2]):
		score += 4
	elif(temp_me[2] == temp_gf[2]):
		score += 2
	elif(temp_me[0] == temp_gf[0]):
		score += 1
	else:
		score -= 5
	
	ansme += str(activity[int(temp_me[0])]) + ":"
	ansme += str(place[int(temp_me[2])])+ ", "
	ansgf += str(activity[int(temp_gf[0])])+ ":"
	ansgf += str(place[int(temp_gf[2])])+ ", "
	
print(ansme[:-2])
print(ansgf[:-2])
if(score >= 7):
	print("Yes! You're my love! : Score is " + str(score) + ".")
elif(score >=0):
	print("Umm.. It's complicated relationship! : Score is "+ str(score) + ".")
else:
	print("No! We're just friends. : Score is "+ str(score) + ".")
