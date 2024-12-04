import os

def act():
    from Activities import ( activity2, activity3, activity4, activity6, activity7, activity8, activity9, activity10, activity11, activity12, activity13, activity14, activity15, activity16, activity17, activity18, activity20)


print("Code Compiler")

def entry(): 
    enter = input("Press Spacebar and Enter to Start... ")
    while enter == "":
        print("Invalid Selection, Please try again")
        enter = input("Press Spacebar and Enter to Start... ")
user_name = input("Enter your name: ")
user_name = entry()
def clean():
    os.system('clear')
clean()
# L KDWH PBVHOI

#++++++++++++++++++++++++++++++++++++++++++++ACTIVITIES+++++++++++++++++++++++++++++++++++++++++++++++++++
def activities_selection():
    global act
    print("++++++++++++++++++++")
    print("Activities Selection")
    print("++++++++++++++++++++")
    print()
    usr = input("Enter the no of which activity you want to access ---> ")
    if usr == "2":
        from Activities import (activity2)
    elif usr == "3":
        from Activities import (activity3)
    else:
        print("+++++++++++++++++++++")
        print("Not a Valid Selection")
        print("+++++++++++++++++++++")
        print()
        input("Press Enter to Continue.....")
        clean()
        return(activities_selection())
    

def choices(a,b,c,d):
    pass
    print(f"Welcome {user_name} to Code Compiler 2000!")
    print("How may I help you today??")
    print(f"[{a}] Activities")
    print(f"[{b}] Code challenges (submitted)")
    print(f"[{c}] Code_challenges (not submitted/missing )")
    print(f"[{d}] code testing/examples from yt")
    print()
    choice = input()
    if choice == "1":
        print("Activities")
        activities_selection()
    elif choice == "2":
        print("Code_challenges:")
    elif choice == "3":
        print("Code_challenges2:")
    elif choice == "4":
        ("yt")
    else:
        print("++++ Invalid Selection, Please Try again ++++")
        print()
        return(choices(a,b,c,d))
choices(1,2,3,4)

print()

