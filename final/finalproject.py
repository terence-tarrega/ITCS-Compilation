import os

def act():
    from Activities import ( activity2, activity3, activity4, 
    activity6, activity7, activity8, 
    activity9, activity10, activity11, activity12, 
    activity13, activity14, activity15, activity16, 
    activity17, activity18, activity20)


def code():
    from Code_challenges import ( code_challenge1, code_challenge2, code_challenge3, code_challenge4, 
    code_challenge5, code_challenge6, code_challenge6_modified, code_challenge7, code_challenge8, 
    code_challenge9, code_challenge10, code_challenge11, code_challenge12,
    code_challenge13, code_challenge14, code_challenge15, code_challenge16 )

def codeM():
    from Code_challenges2 import ( readme )



print("Code Compiler")

def entry(): 
    enter = input("Press Spacebar and Enter to Start... ")
    while enter == "":
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        enter = input("Press Spacebar and Enter to Start... ")
user_name = input("Enter your name: ")
user_name = entry()
def clean():
    os.system('clear')
clean()
# L KDWH PBVHOI

#++++++++++++++++++++++++++++++++++++++++++++ACTIVITIES++++++++++++++++++++++++++++++++++++++++++++++++++++
def activities_selection():
    global act
    print("=============================================")
    print("++++++++++ Activities Selection ++++++++++")
    print("=============================================")
    print()    
    usr = input("Enter the no of which activity you want to access ---> ")
    if usr == "2":
        from Activities import (activity2)
    elif usr == "4":
        from Activities import (activity4)
    elif usr == "6":
        from Activities import (activity6)
    elif usr == "7":
        from Activities import (activity7)
    elif usr == "8":
        from Activities import (activity8)
    elif usr == "9":
        from Activities import (activity9)
    elif usr == "10":
        from Activities import (activity10)
    else:
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        input("Press Enter to Continue.....")
        clean()
        return(activities_selection())
    

#++++++++++++++++++++++++++++++++++++++++++++++CODE_CHALLENGES+++++++++++++++++++++++++++++++++++++++++++++++++

def code_challenges_selection():
    print("=============================================")
    print("++++++++++Code_Challenges Selection++++++++++")
    print("=============================================")
    print()
    usr = input("Enter the no of which Code_Challenges you want to access ---> ")
    if usr == "1":
        from Code_challenges import code_challenge1
    elif usr == "2":
        from Code_challenges import code_challenge2
        usr2 = "Do you want to continue browsing?? [y/n] "
        if usr2.lower == "y":
            from final import (finalproject)
        else:
            print("Alrighty then, Thank you for Browsing in the Code Compiler 2000!! :] ")
    elif usr == "3":
        from Code_challenges import code_challenge3
    elif usr == "4":
        from Code_challenges import code_challenge4
    elif usr == "5":
        from Code_challenges import code_challenge5
    elif usr == "6":
        from Code_challenges import code_challenge6
    elif usr == "7":
        from Code_challenges import code_challenge7
    elif usr == "8":
        from Code_challenges import code_challenge8
    elif usr == "9":
        from Code_challenges import code_challenge9
    elif usr == "10":
        from Code_challenges import code_challenge10
    elif usr == "11":
        from Code_challenges import code_challenge11
    elif usr == "12":
        from Code_challenges import code_challenge12
    elif usr == "13":
        from Code_challenges import code_challenge13
    elif usr == "14":
        from Code_challenges import code_challenge14
    elif usr == "15":
        from Code_challenges import code_challenge15
    elif usr == "16":
        from Code_challenges import code_challenge16
    else:
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        input("Press Enter to Continue.....")
        clean()
        return(code_challenges_selection())

def missing_incomplete_selection():
    global act
    print("==================================================")
    print("++++++++++ Missing/Incomplete Selection ++++++++++")
    print("==================================================")
    print()    
    usr = input("Enter the no of which missing code_challenge you want to access ---> ")
    if usr == "2":
        from Code_challenges2 import (readme)
    else:
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        input("Press Enter to Continue.....")
        clean()
        return(missing_incomplete_selection())



def choices(a,b,c,d):
    pass
    print("=========================================================")
    print(f"++++++++++ Welcome {user_name} to Code Compiler 2000! ++++++++++")
    print("=========================================================")
    print()
    print("++++++++++++++ How may I help you today??? ++++++++++++++")
    print()
    print(f"\t\t[{a}] Activities")
    print(f"\t\t[{b}] Code challenges (submitted)")
    print(f"\t\t[{c}] Code_challenges (not submitted/missing )")
    print(f"\t\t[{d}] code testing/examples from yt")
    print()
    choice = input("Press the no. of the option you want to select:  ")
    if choice == "1":
        clean()
        activities_selection()
        
    elif choice == "2":
        clean()
        code_challenges_selection()
        
    elif choice == "3":
        clean()
        print("Code_challenges2:")
        
    elif choice == "4":
        clean()
        print("yt")
        
    else:
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        return(choices(a,b,c,d))
choices(1,2,3,4)
print()

