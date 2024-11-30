#conditional statements and decisions

money = 0

worker = input("Enter your name >>>")

hasWorked = input("Did you work today?")

#if else statements

if hasWorked.lower() == "yes":
	money += 1
	print(f"Hi {worker}, Today you have a total of {money} money")
else:
	print(f"Hi {worker}, Today you have a total of {money} money")
#para laging lowercase yung tinatype mo dun sa input