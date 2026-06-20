expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            amount, category = line.strip().split(",")
            expenses.append((float(amount), category))
except FileNotFoundError:
    pass
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")

        expenses.append((amount, category))

        with open("expenses.txt", "a") as file:
            file.write(f"{amount},{category}\n")

        print("Expense added successfully!")
        
    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            for idx, (amount, category) in enumerate(expenses, start=1):
                print(f"{idx}. {category}: ${amount:.2f}")
                
    elif choice == '3':
        total = sum(amount for amount, _ in expenses)
        print(f"Total expenses: ${total:.2f}")

    elif choice == '4':
        if not expenses:
            print("No expenses to delete.")
        else:
            for idx, (amount, category) in enumerate(expenses, start=1):
                print(f"{idx}. {category}: ${amount:.2f}")

        delete_index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= delete_index < len(expenses):
            expenses.pop(delete_index)

            with open("expenses.txt", "w") as file:
                for amount, category in expenses:
                    file.write(f"{amount},{category}\n")

            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")  

    elif choice == '5':
        print("Exiting the expense tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")