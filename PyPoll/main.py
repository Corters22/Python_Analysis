import os
import csv

#connecting csv file to code
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #list of candidates voted for and count of total votes
    candidates = []
    total_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        candidates.append(row[2])

    #pulling out unique values of candidates
    set_uni = set(candidates)
    unique_cand = list(set_uni)
    
    #counting how many votes each candidate recieved
    total_cand_vote = []
    for each in unique_cand:
        num_of_votes = 0
        for vote in candidates:
            if each == vote:
                num_of_votes += 1
        total_cand_vote.append(num_of_votes)

#zipping lists of #of votes with candidate name
vote_results = []
final_vote = zip(unique_cand, total_cand_vote)
#calculating vote percentage, and winner
for row in final_vote:
    vote_results.append(row[0] + ": " + f'{((row[1]/total_votes) *100):.3f}' + "% " + "(" + str(row[1]) + ")")
    if row[1] == max(total_cand_vote):
        winner = row[0]        

#printing final results
print("Election Results")
print("-" * 20)
print("Total Votes: " + str(total_votes))
print("-" * 20)
print(vote_results[0])
print(vote_results[1])
print(vote_results[2])
print(vote_results[3])
print("-" * 20)
print("Winner: " + winner)
print("-" * 20)
   

#open new text file
output_path = os.path.join("Analysis", "results.txt")
with open(output_path, 'w', newline='') as textfile:
   
    #print to text file  
    print("Election Results", file=textfile)
    print("-" * 20, file=textfile)
    print("Total Votes: " + str(total_votes), file=textfile)
    print("-" * 20, file=textfile)
    print(vote_results[0], file=textfile)
    print(vote_results[1], file=textfile)
    print(vote_results[2], file=textfile)
    print(vote_results[3], file=textfile)
    print("-" * 20, file=textfile)
    print("Winner: " + winner, file=textfile)
    print("-" * 20, file=textfile)