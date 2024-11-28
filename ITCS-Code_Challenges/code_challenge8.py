#Fetching of 10 numbers
#Gagamitin for summing up numbers
#So user inputs random/specific"Na numbers and the at the same time mag sum up sya dapat
#okay I think
#asignment operator and for loop

#like this?
#okay now add odd even stuff
odd = 0
even = 0
answer = 0

for loop in range(1,11):
   inp = int(input(f"{loop} put the here: "))
   answer += inp
   
   if inp % 2:
      even += 2
   else:
      odd += 1
      
print(f"The sum of the numbers you have given is: {answer}")


print(f"This is even: {even}")
print(f"This is odd: {odd}")
   

