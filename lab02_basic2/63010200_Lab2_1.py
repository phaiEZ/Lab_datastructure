num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
class translator:
    
    
    def deciToRoman(self, number):

        i = 12
        dec = ""
        while number:
            div = number // num[i]
            number %= num[i]

            while div:
                dec += sym[i]
                div -= 1
            i -= 1
        return dec

    def romanToDeci(self, s):
        num = [900, 1000, 400, 500, 90, 100, 40, 50,
           9, 10, 4, 5, 1]
        sym = ["CM", "M", "CD", "D","XC", "C", "XL","L" 
            , "IX", "X","IV", "V","I" ]
        roman = s
        number = 0
        j = 0
        i = 0
        while (roman):
           
            while(1):
               # print(s)
                if sym[i] in roman:
                    # print("found " + sym[i])
                    roman = str(roman).replace(sym[i],"",1)
                    # print(roman)
                    # print(number)
                    number += num[i]
                else:
                    #print("b")
                    break
            
            i += 1
        return number

x = int(input("Enter number to translate : "))
print(translator().deciToRoman(x))
x = translator().deciToRoman(x)
print(translator().romanToDeci(x))