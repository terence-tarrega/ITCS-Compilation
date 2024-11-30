prelim = int(input("What was your score on Prelims? "))

midterms = int(input("What was your score on Midterms? "))

finals = int(input("What was your score on Finals? "))

quiz = int(input("What is your total score on your Quizess? "))

activity = int(input("What is your total score on your Activities? "))

projects = int(input("What is your score on your Project/s? "))

FG = (prelim*0.15)+(midterms*0.15)+(finals*0.15)+(quiz*0.25)+(activity*0.15)+(projects*0.15)//100

if FG >= 75:
	print(f"Congrats you passed! Your Grade is: {FG}")
else:
	print(f"Failed! Your Grade is: {FG}")
print("Thanks for Trying this out!")
