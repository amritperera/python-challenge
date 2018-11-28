import pandas

bd =  pandas.read_csv('budget_data.csv')

total_months = (len(bd.index))

running_total = 0

#Total Net Profit/Loss Calculation
for x in range(total_months):
	running_total = bd.iat[x,1] + running_total

#Average Calculation
average_change = (bd.iat[total_months-1,1] - bd.iat[0,1]) / (len(bd.index)-1)

print("")
print("Financial Analysis")
print("----------------------------")

print(f"Total Months: {total_months}")
print(f"Total: ${running_total}")
print(f"Average Change: ${average_change}")