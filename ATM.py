Balance = 0.00
statement = {"Deposit": 0, "Withdraw": 0}
def checkBalance():
    print("Your bank balance is: ", Balance)

def Deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount > 0:
        global Balance 
        Balance += amount
        print(f"{amount} deposited")
        print("Balance = ",Balance)
        statement["Deposit"] += amount
    else:
        print("Enter a valid amount")

def Withdraw():
    amount = float(input("Enter the amount to be withdrawn: "))
    global Balance
    if amount > 0 and amount <= Balance:
        Balance -= amount
        print(f"{amount} withdrawn")
        print("Balance remains = ", Balance)
        statement["Withdraw"] += amount
    elif amount > Balance:
        print("Insufficient funds")
    else:
        print("Enter a valid amount")

def Statement():
    for transaction in statement:
        print(f"{transaction} = {statement[transaction]}")
    print(Balance)

def ATM():
    while True:
        print("1-> Check Balance")
        print("2-> Deposit")
        print("3-> Withdraw")
        print("4-> Statement")
        print("5-> Exit")
        ch = input("Enter your choice(1-5): ")
        if ch == '1':
            checkBalance()
        elif ch == '2':
            Deposit()
        elif ch == '3':
            Withdraw()
        elif ch == '4':
            Statement()
        elif ch == '5':
            print("Thank you for using the ATM")
            return
        else:
            print("Invalid input")


ATM()