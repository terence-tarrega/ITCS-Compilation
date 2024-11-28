#while loop
import os
tuloy = True
x = 0

print("Enter a number. \nIf you put a 0 in it, then the progarm will terminate and you will get the sum of all the number/s you typed in:")

while tuloy == True:
    number = eval(input("Enter a number--->  "))
    if number == 0:
        os.system('cls')
        print(f"The total of the number/s you entered is : [{x}]")
        print()
        print("::::Program Terminated, Thank You!::::")
        print()
        break
    else:
        x += number
        continue