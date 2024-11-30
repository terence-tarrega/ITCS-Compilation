#Nested conditions???

DLL = input("Are you a student of DLL? (yes/no??) : ")

if DLL.lower() == "yes":
	print("Good Morning Student!","\nWelcome to the DLL Scholarship Form!")

	yearlv = input("What is your current year in DLL?")
	if yearlv.lower() == "freshman":
		print("Hello Freshmen of DLL!")
	elif yearlv.lower() == "sophomore":
		print("Hello Sophomore of DLL!") 
	elif yearlv.lower() == "junior":
		print("Konnichiwa Junior_kun of DLL!")
	elif yearlv.lower() == "senior":
		print("Welcome Senior of DLL!")
	else: 
			print("???")
	youNeed = input("Do you need this scholarship?? (y/n) : ")
	if youNeed.lower() == "yes":
		print ("Scholarship Granted :}")
	else:
		print("Okay thanks for using it")

