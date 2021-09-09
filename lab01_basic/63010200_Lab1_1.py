temph = True
tempm = True
temps = True

print("*** Converting hh.mm.ss to seconds ***")
h,m,s =input("Enter hh mm ss : ").split()

temph = (int(h)>=0)
tempm = (int(m) < 60 and int(m)>=0)
temps = (int(s) < 60 and int(s)>=0)





if((temph and tempm and temps) == True):
    if (int(h) < 10):
        h = "0"+h
    if (int(m) < 10):
        m = "0"+m
    if (int(s) < 10):
        s = "0"+s
    print(h +":"+m+":"+ s + " = " + "{:,}".format((int(s)+int(m)*60+int(h)*3600))+ " seconds")
elif temph == False:
    print("hh("+ str(h) +") is invalid!")
elif tempm == False:
    print("mm("+ str(m) +") is invalid!")
elif temps == False:
    print("ss("+ str(s) +") is invalid!")
