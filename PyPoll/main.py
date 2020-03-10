# ___________________________________ #
# ~ ~ ~   IMPORT SOME MODULES   ~ ~ ~ #

# Import the os module so we can can create a path to the data file
import os

# Import the csv module so we can read the data file
import csv


# _____________________________________ #
# ~ ~ ~   CREATE SOME VARIABLES   ~ ~ ~ #

# Create and initialize the total number of votes cast
total_votes = 0

# Create and initialize a list of candidates who received votes
candidate_names = []

# Create and initialize a list of the total number of votes each candidate won
candidate_votes = []

# Create and initialize variable for identifying the vote total of the winning candidate
winner_votes = 0

# Create and initialize a variable for identifying the name of the winning candidate
winner = ""

# Create a variable for printing the analysis
analysis = ""

# ________________________________________ #
# ~ ~ ~   GRAB AND ANALYZE OUR DATA  ~ ~ ~ #

# Path to collect data from the Resources folder
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

# Split the data on commas
    election_data = csv.reader(csvfile, delimiter=',')
    
   #  Skip the header
    next(election_data)
    
    # Start the loop!
    for vote in election_data:
        
        # Increment the number of votes
        total_votes += 1
        
        # If the current candidate has already received votes, find their position in the list of candidate names and use this value to count this vote
        
        if vote[2] in candidate_names:
            candidate_index = candidate_names.index(vote[2])
            candidate_votes[candidate_index] = int(candidate_votes[candidate_index]) + 1
 
        # If the current candidate hasn't received votes yet, add their name to the list of candidates and count their first vote
        
        else:
            candidate_names.append(vote[2])
            candidate_votes.append("1")


# ______________________________________________ #
# ~ ~ ~   PERFORM ANALYSIS AND PRINT OUPUT ~ ~ ~ #


# Add the overal vote total to the analysis
analysis = "Total Votes: " + str(total_votes)

# Analyze the lists of candidates and their vote totals
for candidate in candidate_names:
    
    # Summarize each candidate's performance
    analysis = analysis + (
        f"\n{candidate}: {round(int(candidate_votes[candidate_names.index(candidate)])/total_votes*100,4)}% ({candidate_votes[candidate_names.index(candidate)]})")
    
    # Find the winner
    if int(candidate_votes[candidate_names.index(candidate)]) > winner_votes:
        winner_votes = int(candidate_votes[candidate_names.index(candidate)])
        winner = candidate


# Add the winner to the analysis
analysis = analysis + (f"\nWinner: {winner}")

# Print the analysis to the terminal
print(analysis)

# ____________________________________________ #
# ~ ~ ~   OUTPUT ANALYSIS TO A NEW FILE ~ ~ ~ #

# Specify the file to write to
output_data = open("data.txt", "w+")

# Print the analysis to the file
output_data.write(analysis)

# Finish storing the file
output_data.close()
