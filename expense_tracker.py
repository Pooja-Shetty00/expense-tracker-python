expenses=[]
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        expenses.append((amount, category))
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
        print("Exiting the expense tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")