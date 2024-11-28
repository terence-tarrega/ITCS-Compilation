prelim = int(input("What is your score?"))

midterms = int(input("What is your score?"))

finals = int(input("What is your score?"))

quiz = int(input("What is your score?"))

activity = int(input("What is your score?"))

projects = int(input("What is your score?"))

FG = (prelim*0.15)+(midterms*0.15)+(finals*0.15)+(quiz*0.25)+(activity*0.15)+(projects*0.15)//100

if FG >= 75:
	print("Congrats you passed! Your Grade is",FG)
else:
	print("Failed! Your Grade is",FG)
print("Thanks")
