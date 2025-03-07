def deposit():
    balance = 0

    while True:
        try:
            amount = float(input("Enter amount to be Deposited: "))
        except ValueError:
            print("Please enter a valid number amount.\n")
            continue
        
        if amount <= 0:
            print("Please enter a number more than 0.\n")
            continue
            
        balance += amount
        print("\nAmount Deposited:", amount)
        return balance

deposit()