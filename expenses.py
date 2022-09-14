

### adding with a loop

# sum = 0
# for expense in expenses:
#     sum = sum + expense
# print("you spent $", sum, " on lunch this week.", sep='')

### using the built-in sum function
# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)
# print("you spent $", total, " on lunch this week.", sep='')


expenses = []
num_expenses = int(input("how many expenses do you have? "))
for i in range(num_expenses):
    expenses.append(float(input("enter expense #" + str(i+1) + ": ")))
total = sum(expenses)
print("you spent $", total, " on lunch this week.", sep='')