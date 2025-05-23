monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expense: "))

monthly_saving = monthly_income - monthly_expenses
projected_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")