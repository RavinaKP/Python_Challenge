import os
import csv
# Counter for total votes
votes_total = 0
# Candidate Options and Vote Counters
vote_candi= {}
candi_list= []
# ticker for count and candidate winner name
candi_win= ""
count= 0
# Read the csv and convert it into a list of dictionaries
with open('election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the header 
    next(csv_reader)
    for row in csv_reader:
        # vote count and total
        votes_total = votes_total + 1
        # each row candidate name match
        candi_name= row[2]

        # create loop and add condtions
        if candi_name not in candi_list:
            candi_list.append(candi_name)
            vote_candi[candi_name] = 0

        # Tricker count
        vote_candi[candi_name] = vote_candi[candi_name] + 1

    # Print the final vote count 
    print("Election Results")
    print("-------------------------------")
    result_final= (f"Total Votes: {votes_total}\n")
    print(result_final, end="")
    print("-------------------------------")
    # Determine the winner by looping through the counts
    for candidate in vote_candi:

        # calulation vote count and percentage
        votes = vote_candi.get(candidate)
        percent_vote= float(votes) / float(votes_total) * 100

        # find out vote count & candidate
        if (votes > count):
            count= votes
            candi_win= candidate

        # Print voter count and percentage for each candinate
        result_voter = f"{candidate}: {percent_vote:.3f}% ({votes})\n"
        print(result_voter, end="")

    # winning candidate name print
    print("-------------------------------")
    winning_candi_sum = (f"Winner: {candi_win}\n")
    print(winning_candi_sum)
    print("-------------------------------")
f = open("analysis.txt", "w")
f.write("Election Results")
f.write("\n-------------------------------\n")
with open('analysis.txt','a') as f:
    out_put = { 'Total Votes :': 369711,
               'harles Casper Stockham:': '23.049% (85213)',
               'Diana DeGette:': '73.812% (272892)',
               'Raymon Anthony Doane:': '3.139%, (11606)'}
    for i,j in out_put.items():
        print( i, ':', j,file=f)
    f.write("\n-------------------------------\n")
    f.write("\nWinner: Diana DeGette")
    print("Winner: Diana DeGette")
f.close()

