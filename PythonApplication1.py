pin = "1234"
opiti = 0

while opiti < 3:
    entered_pin = input("Please, enter your 4-digit PIN: ")    
    if entered_pin == pin:
        print("\nPIN accepted. Welcome to the ATM!")
        break
    else:
        opiti += 1
        remaining = 3 - opiti
        print(f"Incorrect PIN. You have {remaining} attempts left.")
        
        if opiti == 3:
            print("\nIncorrect PIN! You have reached the maximum number of attempts.")
            exit()

    print("-" * 23)

balance = 1000
history = list()

while True:
    print("<<< A T M >>>")
    print("1. Balance check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. History")
    print("5. Exit")
    print()

    a = int(input("Pick option 1-5: "))

    if a == 1:
        print(f"Balance = {balance}lv")

    elif a == 2:
        dep = float(input("Enter Deposit Amount: "))
        balance += dep
        pr1 = f"Successfully added {dep}lv to balance."
        print(pr1)
        print(f"Updated Balance: {balance}")
        history.append(pr1)

    elif a == 3:
        withd = float(input("Enter Withdraw Amount: "))
        balance -= withd
        pr2 = f"Successfully withdrawn {withd}lv from balance."
        print(pr2)
        print(f"Updated Balance: {balance}")
        history.append(pr2)

    elif a == 4:
        print("==== H I S T O R Y ====")
        for i in history:
            print(i)
        print("=" * 23)

    elif a == 5:
        print("Exiting...")
        break

    else:
        continue
    print()
