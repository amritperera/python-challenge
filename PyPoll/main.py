import pandas
import os

csvpath = os.path.join('..','Resources','election_data.csv')
pd =  pandas.read_csv(csvpath)
total_votes = (len(pd.index))

#Output of Total Votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#Output to .txt file
f=open("Election Results.txt","w+")
f.write("Election Results\r\n")
f.write("-------------------------\r\n")
f.write(f"Total Votes: {total_votes}\r\n")
f.write("-------------------------\r\n")
f.close()

list_cand = pd.Candidate.unique()
loop = len(list_cand)

#Loop to Count Each Candidates Votes
count_check = 0
for x in range(0,(loop)):
	count=0
	for y in range(total_votes):

		if pd.iat[y,2] == list_cand[x]:
			count = count+1

	percent_format = '{:.3%}'.format(count/total_votes)		
	print(f"{list_cand[x]}: {percent_format} ({count})")

	f=open("Election Results.txt","a")
	f.write(f"{list_cand[x]}: {percent_format} ({count})\r\n")
	f.close()

	#Running Check of Winner
	if count > count_check:
		winner = list_cand[x]
		count_check = count

#Output of Winner
print("-------------------------\r\n")
print(f"Winner: {winner}\r\n")
print("-------------------------\r\n")

f=open("Election Results.txt","a")
f.write("-------------------------\r\n")
f.write(f"Winner: {winner}\r\n")
f.write("-------------------------\r\n")
f.close()