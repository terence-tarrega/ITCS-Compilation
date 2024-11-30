#Factorial

num = int(input("Enter number: "))
answer = 1
for loop in range(num, 0, -1):
    print(loop)
    answer *= loop
print(f"The factorial of {num} is: {answer}")
