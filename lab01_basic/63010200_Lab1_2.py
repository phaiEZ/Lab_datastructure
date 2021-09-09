print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))


if (x <= 51.99):
    print("Wind classification is Breeze.")
elif(x <= 55.99):
    print("Wind classification is Depression.")
elif(x <= 101.99):
    print("Wind classification is Tropical Storm.")
elif(x <= 208.99):
    print("Wind classification is Typhoon.")
elif(x > 209.0):
    print("Wind classification is Super Typhoon.")