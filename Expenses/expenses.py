#sort an expenses list and get the 3 largest amounts of money spent
#displaying the date and the product for each of the top 3 expenses

spending_list = open('cheltuieli.txt')

class Expense:
    def __init__(self, date, cost, product):
        self.date = date
        self.cost = cost
        self.product = product

    def __repr__(self):
        return repr((self.date, self.cost, self.product))

expenses = []
for line in spending_list:
    stripped_line = line.strip()
    words = stripped_line.split(' ')
    x = Expense(words[0], float(words[1]), words[2])
    expenses.append(x)

sorted_expenses = sorted(expenses, key = lambda x: x.cost, reverse = True)


for i in range(0,3):
    print "In %s, %f were spent on %s." % (sorted_expenses[i].date, sorted_expenses[i].cost, sorted_expenses[i].product)
