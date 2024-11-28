#computation of final grades.py

prelim = eval(input("Prelim Grade >>> "))
midterm = eval(input("Midterm Grade >>> "))
semifinals = eval(input("Semi-Finals Grade >>> "))
finals = eval(input("Finals Grade >>> "))
quiz = eval(input("Quiz Grade >>> "))
project = eval(input("Project Grade >>> "))

if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semifinals >= 65 and semifinals <=100) and (finals >= 65 and finals <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
	FinalG = (prelim * 0.15) + (midterm * 0.15) + (semifinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)
	if FinalG >= 75 and FinalG <= 100:
		print("Congratulations on passing this subject!!")
else:
	print("Error 404 not found")