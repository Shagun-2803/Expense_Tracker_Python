expenses = []

def add_expense(expenses):
  new_expense = {}

  title = input("Enter title of expense: ")
  new_expense["title"]  = title

  category = input("Enter the category: ").lower()
  new_expense["category"] = category

  try:
    amount = int(input("Enter amount: "))

  except ValueError:
    print("Enter valid amount")
    return
  new_expense["amount"] = amount

  expenses.append(new_expense)

  print("Expense added successfully")

def display_expense(expense):
  print(f"Title: {expense['title']}")
  print(f"Category: {expense['category']}")
  print(f"Amount: {expense['amount']}")
  print()

def view_expenses(expenses):
  if(len(expenses)==0):
    print("No expenses added yet!")
    return

  for expense in expenses :
    display_expense(expense)

def total_expense(expenses):

  if(len(expenses)==0):
    print("No expenses found!")
    return

  amount = 0

  for expense in expenses:
    amount += expense['amount']

  print(f"Your total expense is {amount}")

def search_expense_by_title(expenses):
  if(len(expenses)==0):
    print("No expenses added yet!")
    return
  
  search_title = input("Enter the title to be searched: ")

  found = False

  for expense in expenses:
    if(search_title.lower() == expense['title'].lower()):
      print("Expense found: ")
      display_expense(expense)
      found = True

  if(found == False):
    print("Expense not found!")

def search_expense_by_category(expenses):
  if(len(expenses)==0):
    print("No expenses added yet!")
    return
  
  category_search = input("Enter the category to be searched: ")

  found = False

  for expense in expenses:
    if(category_search.lower() == expense['category']):
      print("Expense found: ")
      display_expense(expense)
      found = True

  if(found == False):
    print("Expense not found!")

def delete_expense(expenses):
  if(len(expenses)==0):
    print("No expenses to delete!")
    return
  
  for index,expense in enumerate(expenses , start = 1):
    print(f"{index}: {expense['title']}")

  try:
    choice = int(input("Enter the number of expense to be deleted: "))
  except ValueError:
    print("Enter valid amount")
    return

  if(choice > len(expenses) or choice < 1):
    print("Invalid Input!")
    return
  
  expenses.pop(choice-1)

  print("Expense deleted successfully")

  print("New list: ")
  view_expenses(expenses)

  


def main():
  while(True):
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Search by Title")
    print("5. Search by Category")
    print("6. Delete Expense")
    print("7. Exit")

    try:
      choice = int(input("Enter your choice: "))

    except ValueError:
      print("Enter valid choice")
      continue

    if(choice == 1):
      add_expense(expenses)
    
    elif(choice == 2):
      view_expenses(expenses)
    
    elif(choice == 3):
      total_expense(expenses)

    elif(choice == 4):
      search_expense_by_title(expenses)

    elif(choice == 5):
      search_expense_by_category(expenses)

    elif(choice == 6):
      delete_expense(expenses)

    elif(choice == 7):
      break
    
    else:
      print("Invalid Choice")


  

  


main()



