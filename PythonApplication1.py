balance = 1000
print(f"Balance = {balance}lv")
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
        history.append(pr1)
    elif a == 3:
        withd = float(input("Enter Withdraw Amount: "))
        balance -= withd
        pr2 = f"Successfully withdrawn {withd}lv from balance."
        print(pr2)
        history.append(pr2)
    elif a == 4:
        print("==== H I S T O R Y ====")
        for i in history:
            print(i)
        print("=======================")
    elif a == 5:
        print("Exiting...")
        break
    else:
        continue
    print()
