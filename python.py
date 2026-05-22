expenses = []

def add_expense(expenses):
  new_expense = {}

  title = input("Enter title of expense: ")
  new_expense["title"]  = title

  category = input("Enter the category: ").lower()
  new_expense["category"] = category

  amount = int(input("Enter amount: "))
  new_expense["amount"] = amount

  expenses.append(new_expense)

  print("Expense added successfully")

def view_expenses(expenses):
  if(len(expenses)==0):
    print("No expenses added yet!")
    return

  for expense in expenses :
    print(f"Title: {expense['title']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: {expense['amount']}")
    print()

def total_expense(expenses):

  if(len(expenses)==0):
    print("No expenses found!")
    return

amount = 0

for expense in expenses:
  amount += expense['amount']

print(f"Your total expense is {amount}")

def main():
  while(True):
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
      add_expense(expenses)
    
    elif(choice == 2):
      view_expenses(expenses)
    
    elif(choice == 3):
      total_expense(expenses)

    elif(choice == 4):
      break
    
    else:
      print("Invalid Choice")

main()