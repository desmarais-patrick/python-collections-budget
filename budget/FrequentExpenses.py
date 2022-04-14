import collections
import matplotlib.pyplot as plt

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
#print("Top 5:", top5)
#print("Decomposed:", *top5)
#for i in zip(*top5):
#    print("Zipped'i:", i)

# zip can combine lists i-th elements, like a zipper meeting two or more pins,
#     ex. zip((1, 2), ("a", "b")) ==> (1, "a"), (2, "b")
# zip can take a dictionary and separate keys and values (note the * symbol):
categories, count = zip(*top5)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title("# of Purchases by Category")
plt.show()