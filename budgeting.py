Income = []
Expense = []
while True:
    print("--- Budgeting Menu ---\n")
    budgeting_choice = int(input("What do you wish to do?\n1. Add new Income/Expene\n2. Remove existing Income/Expense\n3. View calendar\n4. Back to main menu\n\nChoice: "))
    if budgeting_choice == 1:
        addition_choice = int(input("What would you like to add?\n1. Income\n2. Expense\n3. Back to main menu\n\nChoice: "))
        if addition_choice == 1:
            Income.append(float(input("Enter the amount of income: ")))
            print("Adding new income...")
        elif addition_choice == 2:
            Expense.append(float(input("Enter the amount of expense: ")))
            print("Adding new expense...")
        else:
            break
    elif budgeting_choice == 2:
        budget_removing_choice = int(input())
        for i, expense in enumerate(Expense):
            print(f"Index {i}: {expense}")
        removing_choice = int(input("Enter the index of the expense to remove: "))
        Expense.pop(removing_choice)
        print("Expense removed.")

    elif budgeting_choice == 4:
        for i, income in enumerate(Income):
            print(f"Index {i}: {income}")
        removing_choice = int(input("Enter the index of the income to remove: "))
        Income.pop(removing_choice)
        print("Income removed.")
    elif budgeting_choice == 5:
        print("On the way")
    elif budgeting_choice == 6:
        break
    else:
        print("Error: Please enter a valid choice!")