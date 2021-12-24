from budget import *
from unittest import main
from budget import create_spend_chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(create_spend_chart([food, clothing, auto]))
print(create_spend_chart([food, clothing]))


main(module='tests', exit=False)


