expenses = [10.50, 8, 5, 15, 20, 5, 3]

### adding with a loop

# sum = 0
# for expense in expenses:
#     sum = sum + expense
# print("you spent $", sum, " on lunch this week.", sep='')

### using the built-in sum function

total = sum(expenses)
print("you spent $", total, " on lunch this week.", sep='')