import os
import csv
csv_election_file= ('../election_data.csv')
with open(csv_election_file,newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)
    #print("csv_header:",csv_header)
    #print("Reading the CSV file ... ")
    
    num_of_votes = 0
    votes_for_each_candidate = {}

    for this_row in csv_reader:
        
        num_of_votes =num_of_votes + 1
        this_candidate_name = this_row[2]

        if this_candidate_name not in votes_for_each_candidate.keys():
            votes_for_each_candidate [this_candidate_name] = 1
        else:
            votes_for_each_candidate [this_candidate_name] += 1
            
         

# File got closed here
# This line after with-clause

max_votes = 0
winner_name = ""
percent_votes={}


for candidate_name in votes_for_each_candidate.keys():
    Vote_for_this_candidate = votes_for_each_candidate[candidate_name]
    
    if Vote_for_this_candidate > max_votes:
        max_votes = Vote_for_this_candidate
        winner_name = candidate_name       
      
    percent_votes[candidate_name] = str(round((votes_for_each_candidate[candidate_name] / num_of_votes)*100,2)) +"%"  

print("Total Numbers of Votes:", num_of_votes)
print("votes_for_each_candidate so far: ", votes_for_each_candidate)
print("List of candidates: ", votes_for_each_candidate.keys())
print("Percentage of Votes:", percent_votes)
print("Winner is : ", winner_name)

with open("results.txt","w") as file:
    file.write("Total Numbers of Votes:" + str(num_of_votes) + "\n")
    file.write("votes_for_each_candidate so far: " + str( votes_for_each_candidate) + "\n") 
    file.write("List of candidates: " + str( votes_for_each_candidate.keys()) + "\n") 
    file.write("Percentage of Votes:" + str( percent_votes) + "\n")
    file.write("Winner is : " + str( winner_name) + "\n")


