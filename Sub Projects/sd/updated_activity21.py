# def like_this(name,age):
#     print(f"Hello Mr. {name}")
#     print(f"your age is {age}")

# like_this("Oswald",22)
# brocode example from yt


print("Code Compiler")

def entry(enter): 
    enter = input("Press Spacebar and Enter to Start... ")
    while enter == "":
        print("Invalid Selection, Please try again")
        enter = input("Press Spacebar and Enter to Start... ")
user_name = input("Enter your name: ")
entry(entry)


# L KDWH PBVHOI

def choices(a,b,c,d):
    pass
    print(f"Welcome {user_name} to Code Compiler 2000!")
    print("How may I help you today??")
    print(f"[{a}] Activities")
    print(f"[{b}] Code challenges (submitted)")
    print(f"[{c}] Code_challenges (not submitted/missing )")
    print(f"[{d}] code testing/examples from yt")
    choice = input()
    if choice == "1":
        pass
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


def activities(actNo1,actNo2,actNo3,actNo4,actNo5,actNo6,actNo7,actNo8,actNo9,actNo10,actNo11,actNo12,actNo13,actNo14,actNo15):
    print("Here's a list of the activities ranging from 1 - 20:")
    for q in range(1,21):
        print(f"Activity1: {actNo1}")
    act = input("Choose an Activity by typing: eg. act1 ---> ")
    if act.lower() == "act1":
        print("MyFirstProgram.py")
        print("Hello Darkness My Old Friend")
    elif act.lower() == "act2":
        name = input("Please enter your last name ---> ")
        print("Good Morning, Good afternoon and or Goodevening Mr./Ms. " + name)
    elif act.lower() == "act3":
        no1 = eval(input("type first number ---> "))
        no2 = eval(input("type second number --> "))
        answer = no1 + no2
        print("the sum of",no1," and ",no2,"is",answer,":)")
    else:
        print("++++ Invalid Selection, Please Try again ++++")
        return(activities())