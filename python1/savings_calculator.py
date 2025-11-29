income = int(input())
expenses = int(input())
savings = income - expenses
if savings > 0.2 * income:
    print("You are saving enough!")
else:
    print("You need to save more.")         