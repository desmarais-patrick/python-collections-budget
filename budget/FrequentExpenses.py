import collections
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories = []
for expense in expenses.list:
    # if expense.category in spending_categories:
    #    continue
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)

# zip can combine lists
# zip can take a dictionary and separate keys and values (note the * symbol):
categories, count = zip(*top5)
print(categories)
print(count)
