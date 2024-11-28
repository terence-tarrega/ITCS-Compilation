for x in range(1,10):
    for y in range(10, x, -1):
        print(" ",end=" ")
    for z in range(1, x+1):
        print("*", end=" ")
    for a in range(1, x+1):
        print("*", end=" ")
    print()


for x in range(1,10):
    for y in range(1, x+1):
        print(" ",end=" ")
    for z in range(10, x,-1):
        print("*", end=" ")
    for a in range(10, x,-1):
        print("*", end=" ")
    print()

#baliktad
#edit: problem solved 