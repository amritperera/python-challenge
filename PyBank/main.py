import pandas
import os

csvpath = os.path.join('..','Resources','budget_data.csv')

bd =  pandas.read_csv(csvpath)
total_months = (len(bd.index))
running_total = 0

#Total Net Profit/Loss Calculation
for x in range(total_months):
	running_total = bd.iat[x,1] + running_total

#Average Calculation
average_change = (bd.iat[total_months-1,1] - bd.iat[0,1]) / (len(bd.index)-1)

#Greatest Increase Calculation
check = 0
for x in range(total_months-1):
	g_incTest = bd.iat[x+1,1] - bd.iat[x,1]
	if g_incTest > check:
		date = bd.iat[x+1,0]
		g_inc = g_incTest
		check = g_incTest

#Greatest Decrease Calculation
check = 0
for x in range(total_months-1):
	g_decTest = bd.iat[x+1,1] - bd.iat[x,1]
	if g_decTest < check:
		date2 = bd.iat[x+1,0]
		g_dec = g_decTest
		check = g_decTest

#Format Some Variables
average_change = '${:,.2f}'.format(average_change)
#Output
print("")
print("Financial Analysis")
print("----------------------------")

print(f"Total Months: {total_months}")
print(f"Total: ${running_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {date} (${g_inc})")
print(f"Greatest Decrease in Profits: {date2} (${g_dec})")

#Output to New text file if there isn't one already
f = open("Financial Analysis.txt","w+")

f.write("")
f.write("Financial Analysis\r\n")
f.write("----------------------------\r\n")

f.write(f"Total Months: {total_months}\r\n")
f.write(f"Total: ${running_total}\r\n")
f.write(f"Average Change: {average_change}\r\n")
f.write(f"Greatest Increase in Profits: {date} (${g_inc})\r\n")
f.write(f"Greatest Decrease in Profits: {date2} (${g_dec})\r\n")

f.close()