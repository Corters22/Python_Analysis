import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    
    candidates = []
    total_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        candidates.append(row[2])

    set_uni = set(candidates)
    unique_cand = list(set_uni)
    total_cand_vote = []
    
    for each in unique_cand:
        num_of_votes = 0
        for vote in candidates:
            if each == vote:
                num_of_votes += 1
        total_cand_vote.append(num_of_votes)


    final_vote = zip(unique_cand, total_cand_vote)
    for row in final_vote:
        print(row[0] + ": " + f'{((row[1]/total_votes) *100):.3f}' + "% " + "(" + str(row[1]) + ")")
        if row[1] == max(total_cand_vote):
            winner = row[0]        

print("Election Results")
print("-" * 20)
print("Total Votes: " + str(total_votes))
print("-" * 20)

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
    print(vote_results(), file=textfile)
    print("-" * 20, file=textfile)
    print("Winner: " + winner, file=textfile)
    print("-" * 20, file=textfile)