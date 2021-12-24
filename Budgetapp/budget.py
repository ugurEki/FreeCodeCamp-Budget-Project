class Category:

  """
  Category class instantiate objects based on different budget categories like 
  food, clothing, and entertainment.
  """
  

  def __init__(self, name):
    self.name = name
    # this instance variable to keep records such as amount of transaction and description. 
    self.ledger = []


  def deposit(self, amount, description = ""):

    """This method that accepts an amount and description."""

    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, withdraw_amount, description = ""):

    """A withdraw method that is similar to deposit method, however 
       the amount passed in should be stored in the ledger as a negative number."""

    if self.check_funds(withdraw_amount) == False:
      return False
    else:
      self.ledger.append({"amount": -withdraw_amount, "description": description})
      return True


  def get_withdraw(self):

    """This method is to calculate the total withdraws of object"""

    total = 0
    for item in self.ledger:
      if item['amount'] < 0:
        total += item['amount']
    return total

    
  def get_balance(self):

    """returns the current balance of the budget category based on 
       the deposits and withdrawals that have occurred
    """

    total = 0
    for amount in self.ledger:
        total += amount['amount']

    return total

  def transfer(self, transfer_amount, category):

    """This method is to transfer from this deposit to other deposit."""

    if self.check_funds(transfer_amount) == False:
      return False

    else:
      self.ledger.append({"amount": -transfer_amount, "description": f"Transfer to {category.name}"})
      category.ledger.append({"amount": transfer_amount, "description": f"Transfer from {self.name}"})
      return True
  
  def check_funds(self, fund_amount):

    """This method that accepts an amount as an argument and check the funds.
       Return False if the amount is greater than the balance of the budget category.
       True otherwise."""

    if self.get_balance() < fund_amount:
        return False
    return True

  def __str__(self):
    star_number = (30 - len(self.name))//2
    title = f"{'*'*star_number + self.name + '*'*star_number}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      total += item['amount']
    output = title + items + "Total: " + str(total)
    return output


def percentages(categories):
  total = 0
  withdraws = []
  results = []
  for category in categories:
    total += category.get_withdraw()
    withdraws.append(category.get_withdraw())
  for withdraw in withdraws:
    results.append(round((withdraw/total) * 100))

  return results

def name_manipulation(categories):
  names = []
  for category in categories:
    names.append(category.name)
  result_string = ""
  longest_name = max(names, key=len)

  for num in range(len(longest_name)):
    string = '     '
    for name in names:
      if num >= len(name):
        string += "   "
      else:
        string += name[num] + "  "

    if (num != len(longest_name) - 1):
      string += '\n'

    result_string += string

  return result_string

def create_spend_chart(categories):

  """Create a bar chart as a string"""
  
  percentage = percentages(categories)
  result = "Percentage spent by category\n"
  i = 100
  while i>= 0:
    string = " "
    for number in percentage:
      if number >= i:
        string += "o  "
      else:
        string += "   "
    result += str(i).rjust(3) + "|" + string + "\n"
    i -= 10

  short_lines = len(categories) * "---" + "-"

  name_manip = name_manipulation(categories)

  result += short_lines.rjust(len(short_lines)+4) + "\n" + name_manip

  return result





