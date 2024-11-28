import os

isTuloy = True
no = 0


for x in range (1, 6):
    for repeat in range (1 , no + 1):
        for y in range (1 , x + 1):
            print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
            print()
            
while isTuloy == True:
    ask = input("Would you like to add a triangle [y/n?] -----> ")

    if ask.lower() == "no":
        print()
        print("::::PROGRAM TERMINATED::::")
        print()
        break
        isTuloy = False
    if ask.lower() == "n":
        print()
        print("::::PROGRAM TERMINATED::::")
        print()
        break
        isTuloy = False
    if ask.lower() == "yes":
        os.system('cls')
        no += 1
        for x in range (1, 6):
            for repeat in range (1 , no + 1):
                for y in range (1 , x + 1):
                    print("*", end=" ")
                for z in range (6, x, -1):
                    print(" ",end=" ")
            print()
    if ask.lower() == "y":
        os.system('cls')
        no += 1
        for x in range (1, 6):
            for repeat in range (1 , no + 1):
                for y in range (1 , x + 1):
                    print("*", end=" ")
                for z in range (6, x, -1):
                    print(" ",end=" ")
            print()
    else:
        print("Invalid Selection! Try again...")
        continue

