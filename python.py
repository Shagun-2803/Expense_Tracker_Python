
def add_expense(expenses):
  new_expense = {}
  title = input("Enter title of expense: ")
  new_expense["title"]  = title
  category = input("Enter the category: ").lower()
  new_expense["category"] = category
  amount = int(input("Enter amount: "))
  new_expense["amount"] = amount
  expenses.append(new_expense)
  print("Expence added successfully")



expenses = []




while(True):
  print("\n1. Add Expense")
  print("2. View Expense")
  print("3. Exit")
  choice = int(input("Enter your choice: "))
  if(choice == 1):
    add_expense(expenses)
  if(choice == 3):
    break
  if(choice > 3 or choice <= 0):
    print("Invalid Choice")