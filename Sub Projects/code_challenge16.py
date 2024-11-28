import os

def ph_denomination_breakdown(amount):
    libo = amount // 1000
    lc = amount % 1000
    hf = lc // 500
    lc = lc % 500
    ht = lc // 200
    lc = lc % 200
    h = lc // 100
    lc = lc % 100
    f = lc // 50
    lc = lc % 50
    t = lc // 20
    lc = lc % 20
    ten = lc // 10
    lc = lc % 10
    print("\nDenomination breakdown:")
    print(f"{libo} - 1000 PHP")
    print(f"{hf} -  500 PHP")
    print(f"{ht} -  200 PHP")
    print(f"{h} -  100 PHP")
    print(f"{f} -   50 PHP")
    print(f"{t} -   20 PHP")
    print(f"{ten} -   10 PHP")
    print(f"{lc} -    1 PHP")

def deposit_money(accounts):
    name = input("Enter your account name: ").strip()
    if name not in accounts:
        print("Account does not exist.")
        return
    while True:
        try:
            deposit_amount = int(input("Enter amount to deposit: "))
            if deposit_amount > 0:
                break
            print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    accounts[name] += deposit_amount
    print(f"{deposit_amount} deposited successfully. New balance: {accounts[name]}")
    ph_denomination_breakdown(deposit_amount)

def withdraw_money(accounts):
    name = input("Enter your account name: ").strip()
    if name in accounts:
        while True:
            try:
                withdraw_amount = int(input("Enter amount to withdraw: "))
                if withdraw_amount > 0:
                    break
                else:
                    print("Withdraw amount must be positive.")
            except:
                print("Invalid input. Enter a numeric value.")
        if accounts[name] >= withdraw_amount:
            accounts[name] -= withdraw_amount
            print(f"{withdraw_amount} withdrawn successfully. New balance: {accounts[name]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account does not exist.")

def create_account(accounts):
    name = input("Enter your name: ").strip()
    if name in accounts:
        print("Account already exists.")
        return
    while True:
        try:
            initial_deposit = int(input("Enter initial deposit: "))
            if initial_deposit >= 0:
                break
            print("Deposit must be non-negative.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    accounts[name] = initial_deposit
    print(f"Account created for {name} with initial deposit of {initial_deposit}.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bank_simulation():
    accounts = {}
    while True:
        clear_screen()
        print("\nWelcome to the Bank Simulation Menu:")
        print("1. Create New Account")
        print("2. Deposit") 
        print("3. Withdraw")
        print("4. Check Balance") #check how much did the user put in the account
        print("5. Exit") #program termination
        choice = input("Choose an option: ")
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit_money(accounts)
        elif choice == '3':
            withdraw_money(accounts)
        elif choice == '4':
            name = input("Enter your account name: ").strip()
            if name in accounts:
                print(f"Current balance for {name}: {accounts[name]}")
            else:
                print("Account does not exist.")
        elif choice == '5':
            print("Exiting program. Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please try again.")
        input("\nPress Enter to continue...") 

bank_simulation()
