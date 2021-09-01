# Data needed for analysis
# 1.  The total number of votes cast.  
# 2.  A complete list of candidates that received votes.
# 3.  The percentage of votes each candidate received.
# 4.  The total number of votes each candidate received.  
# 5.  The winner of the election based on popular votes. 

# Add dependencies.  
import csv
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Skill Drill:  Write "Counties in the Election" with a dashed line below it.  
     txt_file.write("Counties in the Election\n------------------------\n")
     # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")

print('1---------------')
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


txt_file.close()
print('2---------------')

print('4----------------------')







