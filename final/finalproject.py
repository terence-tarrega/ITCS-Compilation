import os

def act():
    from Activities import ( activity1,activity2, activity3, activity4, 
    activity6, activity7, activity8, 
    activity9, activity10, activity11, activity12, 
    activity13, activity14, activity15, activity16, 
    activity17, activity18, activity20)


def code():
    from Code_challenges import ( code_challenge1, code_challenge2, code_challenge3, code_challenge4, 
    code_challenge5, code_challenge6, code_challenge6_modified, code_challenge7, code_challenge8, 
    code_challenge9, code_challenge10, code_challenge11, code_challenge12,
    code_challenge13, code_challenge14, code_challenge15, code_challenge16 )


def ref():
    from References import (loadscreen)






def Logout():
    print("===============================================================")
    print("==================== EXIT PROGRAM SELECTED ====================")
    print("===============================================================")
    print()
    ask = input("Are you sure you want to Close/Exit the Program?? [y/n]: ")
    while ask == "y":
        clean()
        print("==============================================================")
        print("++++++++++ PROGRAM TERMINATED HAVE A NICE DAY ++++++++++++++++")
        print("==============================================================")
        print()
        break
    else:
        clean()
        return(choices(1,2,3,0))



ref()
print("=========================")
print("===== Code Compiler =====")
print("=========================")
def entry(): 
    enter = input("Press Enter to Start... ")
    ref()
    while enter == " ":
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        enter = input("Press Enter to Start... ")
print()
nameUser = input("Enter user name: ")

def clean():
    os.system('clear')
clean()
# L KDWH PBVHOI


#++++++++++++++++++++++++++++++++++++++++++++ACTIVITIES++++++++++++++++++++++++++++++++++++++++++++++++++++
def activities_selection():
    global act
    print("=============================================================")
    print("++++++++++++++++++ ACTIVITIES SELECTION +++++++++++++++++++++")
    print("=============================================================")
    print()    
    usr = input("Enter the no of which activity you want to access ---> ")
    if usr == "1":
        from Activities import (activity1)
    elif usr == "2":
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
    global back
    print("\t\t\b\b\b\b====================================================")
    print("\t\t\b\b\b\b++++++++++ Code_Challenges Selection +++++++++++++++")
    print("\t\t\b\b\b\b====================================================")
    print("""   ___________________________________________________________________
 / \                                                                  \.
|   |                                                                 |.
 \_ |      [ 1] Code Challenge  1         [ 9] Code Challenge  9      |.
    |      [ 2] Code Challenge  2         [10] Code Challenge 10      |.
    |      [ 3] Code Challenge  3         [11] Code Challenge 11      |.
    |      [ 4] Code Challenge  4         [12] Code Challenge 12      |.
    |      [ 5] Code Challenge  5         [13] Code Challenge 13      |.
    |      [ 6] Code Challenge  6         [14] Code Challenge 14      |.
    |      [ 7] Code Challenge  7         [15] Code Challenge 15      |.
    |      [ 8] Code Challenge  8         [16] Code Challenge 16      |.
    |                                                                 |.
    |   ______________________________________________________________|___
    |  /                                                                 /.
    \_/dc_______________________________________________________________/.
""")
    print("note: Press 0 to go back to the main menu :3")
    usr = input("Enter the no of which Code_Challenges you want to access ---> ")
    if usr == "0":
        back()
    elif usr == "1":
        from Code_challenges import code_challenge1
        back()
    elif usr == "2":
        from Code_challenges import code_challenge2
        back()
    elif usr == "3":
        from Code_challenges import code_challenge3
        back()
    elif usr == "4":
        from Code_challenges import code_challenge4
        back()
    elif usr == "5":
        from Code_challenges import code_challenge5
        back()
    elif usr == "6":
        from Code_challenges import code_challenge6
        back()
    elif usr == "7":
        from Code_challenges import code_challenge7
        back()    
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

def back():
    global code_challenges_selection, choices
    usr2 = input("Do you want to continue browsing?? [y/n]: ").strip().lower()
    if usr2 == "n":
        clean()
        choices(1, 2, 3, 0)  # Go back to the main menu
    elif usr2 == "y":
        clean()
        code_challenges_selection()  # Return to code challenges selection
    else:
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        back()  # Retry until valid input is provided


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++ CHOICES +++++++++++++++++++++++++++++++++++++++++++++

def choices(a,b,c,d,):
    global ref
    print("=========================================================")
    print(f"++++++++++ Welcome {nameUser} to Code Compiler 2000! ++++++++++")
    print("=========================================================")
    print()
    print("++++++++++++++ How may I help you today??? ++++++++++++++")
    print("|                                                       |")
    print(f"| [{a}] Activities                                        |")
    print(f"| [{b}] Code challenges (submitted/missing)               |")
    print(f"| [{c}] References Used                                   |")
    print(f"| [{d}] Exit Program                                      |")
    print("|                                                       |")
    print("=========================================================")
    print()
    choice = input("Press the number from [0-3] of the option that you want to select: ")
    if choice == "1":
        clean()
        ref()
        activities_selection()
        
    elif choice == "2":
        clean()
        ref()
        code_challenges_selection()
        
    elif choice == "3":
        clean()
        ref()
        
    elif choice == "0":
        clean()
        Logout()
        
    else:
        print("===========================================================")
        print("++++++++++ Invalid Selection, Please try again ++++++++++")
        print("===========================================================")
        print()
        return(choices(a,b,c,d))
choices(1,2,3,0)
print()


