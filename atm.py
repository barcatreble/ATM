pin = "1234"
opiti = 0

while opiti < 3:
    entered_pin = input("Please, enter your 4-digit PIN: ")

    if not entered_pin.isdigit() or len(entered_pin) != 4:
        print("Invalid PIN format. Must be a 4-digit number.")
        opiti += 1
        remaining = 3 - opiti
        print(f"You have {remaining} attempts left.")

        if opiti == 3:
            print("\nIncorrect PIN! You have reached the maximum number of attempts.")
            exit()
        print("-" * 23) 
        continue
               
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

    try:
        a = int(input("Pick option 1-5: "))
    except ValueError:
        print("Please, write only numbers!\n")
        continue

    if a == 1:
        print(f"Balance = {balance}lv")

    elif a == 2:
        try:
            dep = float(input("Enter Deposit Amount: "))
            if dep < 0:
                print("You must deposit positive amount!\n")
                continue
        except ValueError:
            print("Please, write only numbers!\n")
            continue

        balance += dep
        pr1 = f"Successfully added {dep}lv to balance."
        print(pr1)
        print(f"Updated Balance: {balance}")
        history.append(pr1)

    elif a == 3:
        try:
            withd = float(input("Enter Withdraw Amount: "))
        except ValueError:
            print("Please, write only numbers!\n")
            continue

        if balance < withd:            
            print("Insufficient funds! Try again!\n")
        else: 
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
        print("Option not available! Try again!")
        continue
    print()