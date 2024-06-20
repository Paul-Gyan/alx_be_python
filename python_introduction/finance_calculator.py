month_income = int(input("Enter your monthly income: "))
month_expenses = int(input("Enter your total monthly expenses: "))
month_savings = month_income - month_expenses
print("Your monthly savings are $",month_savings)

projected_savings = (month_savings * 12) + (month_savings * 12 * 0.05)
print("Projected savings after on year,with interest,is: $",projected_savings)