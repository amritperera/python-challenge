import pandas

pd =  pandas.read_csv('election_data.csv')
total_votes = (len(pd.index))

#Output of Total Votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

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
	#Running Check of Winner
	if count > count_check:
		winner = list_cand[x]
		count_check = count

#Output of Winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")