import csv

# Initialize variables
total_months = 0
total_profit_losses = 0
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
previous_profit_loss = 0

# Read the CSV file
with open('budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Calculate total months and total Profit/Losses
        total_months += 1
        total_profit_losses += int(row[1])

        # Calculate monthly changes and find greatest increase and decrease
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            monthly_changes.append(change)
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Print and write results to a text file
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_losses}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

print(output)

with open('financial_analysis.txt', 'w') as file:
    file.write(output)