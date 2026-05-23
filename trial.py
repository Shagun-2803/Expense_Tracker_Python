import json

expenses = [
  {
    "title" : "Pizza",
    "category" : "Food",
    "amount" : 399
  }
]

with open("expenses.json","a") as file:
  json.dump(expenses,file)