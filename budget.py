class Category:
  def __init__(self,name):
    self.name=name
    self.ledger=list()

  def __str__(self):
    op = self.name.center(30, "*") + "\n"
    for i in self.ledger:
      op += f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
    op += f"Total: {format(self.get_balance(), '.2f')}"
    return op


  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False
  
  def get_balance(self):
    total_cash=0
    for i in self.ledger:
      total_cash+=i['amount']
    return total_cash

  def transfer(self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to "+category.name)
      category.deposit(amount,"Transfer from "+self.name)
      return True
    else:
      return False

  def check_funds(self,amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False

def create_spend_chart(categories):
  category_names = []
  spent = []
  perc = []

  for category in categories:
    total = 0
    for i in category.ledger:
      if i['amount'] < 0:
        total -= i['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    perc.append(round(amount / sum(spent), 2)*100)

  title = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    title += str(label).rjust(3) + "| "
    for percent in perc:
      if percent >= label:
        title += "o  "
      else:
        title += "   "
    title += "\n"

  title += "    ----" + ("---" * (len(category_names) - 1))
  title += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        title += name[i] + "  "
      else:
        title += "   "
    if i < longest_name_length-1:
      title += "\n     "

    

  return(title)