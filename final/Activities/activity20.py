Tuloy = True
nt = 0

import os

while Tuloy == True:
    ask = input("Would you like to add a triangle?")
    if ask.lower() == "no":
        print("==========================")
        print("=== Program Terminated ===")
        print("==========================")
        break
        Tuloy = False
    elif ask.lower() == "yes":
        os.system('clear')
        nt += 1 
        for x in range (1,5):
            for y in range (1,nt,+1):
                for z in range (1,x+1):
                    print("*", end=" ")
                for a in range (5,x,-1):
                    print(" ", end=" ")
            print()
        continue
    else:
        print("=================")
        print("====Try Again====")
        print("=================")