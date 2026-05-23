This is my first python project. 
Expense Tracker!

A simple command-line expense tracker built with Python. It lets you log, view, search, and manage your personal expenses right from the terminal. Data is saved to a JSON file so your expenses persist between sessions.

Features:
|   | Feature | Description |
|---|---------|-------------|
| 1 | Add Expenses | Log a new expense with a title, category, and amount |
| 2 | View Expenses | Display all recorded expenses |
| 3 | Total Expense | Calculate and display the sum of all expenses |
| 4 | Search by Title | Find a specific expense by its title |
| 5 | Search by Category | View all expenses under a given category |
| 6 | Delete Expense | Remove an expense by selecting it from a numbered list |


Usage:
When you run the program, you'll see a menu:
1. Add Expense
2. View Expense
3. Total Expense
4. Search by Title
5. Search by Category
6. Delete Expense
7. Exit
   
1. Add Expense
Enter a title, category, and amount. The expense is saved immediately to expenses.json.
Enter title of expense: Coffee
Enter the category: food
Enter amount: 150
Expense added successfully
2. View Expenses
Displays all stored expenses one by one:
Title: Coffee
Category: food
Amount: 150
3. Total Expense
Sums up the amount field across all expenses and prints the total.
4. Search by Title / Category
Case-insensitive search — finds and displays any matching expense(s).
5. Delete Expense
Lists all expenses with numbers. Enter the number of the expense to remove it. The updated list is shown after deletion.

Concepts Practiced:
Being a first Python project, this covers:
1.  Functions and modular code
2.  Lists and dictionaries
3.  File I/O with JSON (json.load, json.dump)
4.  Exception handling (try / except ValueError)
5.  Loops — while for the menu, for to iterate expenses
6.  enumerate() for indexed display
7.  String methods (.lower() for case-insensitive search)



