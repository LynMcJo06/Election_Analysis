# Data needed for analysis
# 1.  The total number of votes cast.  
# 2.  A complete list of candidates that received votes.
# 3.  The percentage of votes each candidate received.
# 4.  The total number of votes each candidate received.  
# 5.  The winner of the election based on popular votes. 

# Add dependencies.  
import csv
import os
# Practice writing to a text file.  
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World\n")

    # Skill Drill:  Write "Counties in the Election" with a dashed line below it.  
    txt_file.write("Counties in the Election\n------------------------\n")
    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

print('1--------------------')

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.  
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate list.
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.  
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # print(row)
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Print the total votes.
    # print(total_votes)

    # Print the candidate list.
    # print(candidate_options)

    # Print the candidate vote dictionary.
    print(candidate_votes)

    
    
# Close the file
txt_file.close()



