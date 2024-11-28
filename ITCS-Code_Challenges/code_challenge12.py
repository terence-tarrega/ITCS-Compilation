for x in range(1,5):
    for y in range(10, x, -1):
        print(" ",end=" ")
    for z in range(1, x+1):
        print("*", end=" ")
    for a in range(1, x+1):
        print("*", end=" ")
    print()

for x in range(1,6):
    # for y in range(11,x):
    #     print("#",end=" ")
    for z in range(14, y,-1):
        print(" ", end=" ")
    for a in range(7, y,-1):
        print("*", end=" ")
    print()