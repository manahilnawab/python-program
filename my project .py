import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("===== Smart Budget Advisor =====")

# Lists to store data
names = []
income_list = []
expenses_list = []
savings_list = []
advice_list = []

# Number of users
n = int(input("Enter number of users: "))

for i in range(n):
    print(f"\nUser {i+1}")
    name = input("Enter name: ")
    income = int(input("Enter monthly income: "))
    expenses = int(input("Enter monthly expenses: "))

    savings = income - expenses

    # Budget advice logic
    if expenses > income:
        advice = "Overspending - Reduce expenses"
    elif savings < income * 0.2:
        advice = "Low savings - Save more"
    else:
        advice = "Good budget management"

    # Store data
    names.append(name)
    income_list.append(income)
    expenses_list.append(expenses)
    savings_list.append(savings)
    advice_list.append(advice)

# NumPy analysis
income_arr = np.array(income_list)
expenses_arr = np.array(expenses_list)
savings_arr = np.array(savings_list)

avg_income = np.mean(income_arr)
avg_expenses = np.mean(expenses_arr)
avg_savings = np.mean(savings_arr)

# Pandas DataFrame
df = pd.DataFrame({
    "Name": names,
    "Income": income_arr,
    "Expenses": expenses_arr,
    "Savings": savings_arr,
    "Advice": advice_list
})

print("\n===== Smart Budget Report =====")
print(df)

print("\n===== Budget Analysis =====")
print("Average Income:", avg_income)
print("Average Expenses:", avg_expenses)
print("Average Savings:", avg_savings)

# Save report
df.to_csv("smart_budget_report.csv", index=False)
print("\nReport saved as smart_budget_report.csv")

# =====================
# Matplotlib Graphs
# =====================

# Income vs Expenses bar chart
plt.figure()
plt.bar(names, income_arr)
plt.bar(names, expenses_arr)
plt.xlabel("Users")
plt.ylabel("Amount")
plt.title("Income vs Expenses")
plt.show()

# Savings line graph
plt.figure()
plt.plot(names, savings_arr, marker='o')
plt.xlabel("Users")
plt.ylabel("Savings")
plt.title("Savings Trend")
plt.show()
