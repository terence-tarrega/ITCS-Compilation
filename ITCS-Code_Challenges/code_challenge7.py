print("Welcome to Mini Mart Simulator!!")
pass
#food products use brackets here 
products = ["Oranges", "Bread", "Butter", "Eggs", "Cheese", "Whole chicken"]

#search google for prices here and also use brackets for listing
prices = [3.00, 2.50, 1.75, 2.00, 4.00, 197.80]

#list actual products here like for print 
print("\nHere are the current available products to choose from!")
print("1. Oranges: ₱3.00")
print("2. Monay: ₱20.00")
print("3. Canton: ₱25.00")
print("4. Eggs: ₱2.00")
print("5. Cheese: ₱4.00")
print("6. Whole chicken: ₱197.80")

total_price = 0.0

#make calc here?? should i put pass above first?? hm?
selected_products = int(input("Enter the number of the product you want to buy 1-5 or 0 to exit: "))-1

if selected_products == -1:
	"break"

if 0 <= selected_products < len(products):
            quantity = int(input("Enter the quantity: "))
            total_price += prices[selected_products] * quantity
else:
	print("Invalid product selection.")


# For User input
age = int(input("Enter your age: "))
t_amount = float(input("Enter the total amount of your purchase: ₱"))
discount = 0

# discount list
if age < 0:
    print("Invalid age.")
else:
    if age < 18:
        discount = t_amount * 0.10  # minor discount I guess
    elif age >= 65:
        discount = t_amount * 0.15  # senior discount
    elif age > 120:
          print("Too old")
    else:
        discount = 0  # No discount

    # Calculate the final price
    final_price = t_amount - discount

    print(f"The final price after discount is: ₱{final_price:.2f}")






























































































#ps to future self: try to add design next time. 
#update: can't add that, late na eh