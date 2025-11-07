monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your monthly expenses: '))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)
print(f'Your monthly savings are: {monthly_savings}')
print(f'Your projected annual savings with interest is: {projected_savings}')