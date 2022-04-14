from . import Expense

class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
        # Define "overage" : an excess or surplus, especially the amount by which a sum of money is greater than a previous estimate.
    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return len(self.expenses) + len(self.overages)

    def __iter__(self):
        pass

    def __next__():
        pass


def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    print("The count of all expenses: ", str(len(myBudgetList)))

if __name__ == "__main__":
    main()