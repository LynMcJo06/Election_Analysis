# Election_Analysis
## Background
In this module, I will be learning and using Python 3 programming language to perform an analysis on election results.  I will be assisting a Colorado Board of Elections employee Tom in an election audit.  I will be responsible for calculating the total votes cast, the total votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote.  
### Lesson 1
This lesson consisted of learning about the command line, installing Python, installing GitBash, setting up a python environment, installing Visual Studio Code (VS Code), and creating and cloning a GitHub repository.  
### Lesson 2
Lesson two was about learning Python.  We created and executed a Python file, learned about data types, performed calculations, were introduced to data structures, decision statement, membership and logical operators, repetition statements and printing formats.  
### Lesson 3
I imported and inspected the election data file and learned the importance of pseudocode.  I have a roadmap for the project; I need to retreive the following data:  
  * The total number of vosts cast
  * A complete list of the candidates that received votes
  * The percentage of votes received for each candidate
  * The total number of votes each candidate received
  * The overall winner of the election as per the popular vote

### Lesson 4
I also about dependencies, modules and packages in Python.  I opened and read a file using both the direct path and indirect path processes.  Then I wrote to a text file and read the election results CSV file.  
### Lesson 5
In this lesson I determined the total number of votes cast in the election, which was 369,711 votes.  I retreived the names of the individual candidate in the election:  Charles Casper STockham, Diana DeGette, and Raymon Anthony Doane.  Next, I determined the vote count for each candidate:  Stockham = 85,213, DeGette = 272,892, and Doane = 11,606.  After determining the total votes cast and the number of votes for each candidate, I calculated the percentage of votes each candidate received, which were:  
  * Stockham = 23.0%
  * DeGette = 73.8%
  * Doane = 3.1%

The winning candidate was Diana DeGette, who received 272,892 votes for a winning percentage of 73.8%.  
### Lesson 6
I made changes to the original code so that the election results would print to the terminal and to a text file.  The directions in the module were extremely confusing.  I also had trouble with VS Code not allowing me indent and comment out certain lines of code.  

## Summary
The election analysis showed the following:
 - Approximately 369,711 votes were cast in the election.  
 - Three candidates received votes: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.  
 - The results were:
 -      * Charles Stockham received 85,213 votes and 23.0% of the votes cast
 -      * Diana DeGette received 272,892 votes and 73.8% of the votes cast
 -      * Raymon Doane received 11,606 votes and 3.1% of the votes cast.  
 - The winner of the election was Diana DeGette, who received 73.8% of the popular vote.  

# CHALLENGE
## Scope
I assisted a Colorado Board of Elections (CBOE) employee in an audit of the tabulated results for a U.S. congressional precinct in Colorado.  The work to be performed is as follows:
 * Determine the total number of votes cast
 * The total number of votes for each candidate
 * The percentage of votes for each candidate
 * The winner of the election by popular vote
 * The voter turnout for each county
 * The percentage of votes from each county
 * The county with the highest turnout

The CBOE would like this audit to be automated so it can be used in future elections.  This vote count report will be used to certify this U.S. congressional race.  
##  Election Audit Results
The total number of votes cast were 369,711.  
Three candidates received votes:  
 * Diana DeGette
 * Raymon Anthony Doane 
 * Charles Casper Stockham

Ms. Diana DeGette received 272,892 votes that equates to 73.8% of the votes cast.  Mr. Raymon Doane received 11,606 votes or 3.1% of the total votes cast.  Mr. Charles Stockham received 85,213 votes or 23.0% of the total votes cast.  The following table summarizes the results:  

Diana DeGette:           73.8%        272,892
Raymon Anthony Doane:     3.1%         11,606
Charles Casper Stockham: 23.0%         85,213

Three counties comprised this precinct:  
- Arapahoe
- Denver
- Jefferson


The following table summarizes the percentage of votes from each county and the voter turnout for each county:  
Arapahoe:     6.7%    24,801
Denver:      82.8%   306,055
Jefferson:   10.5%    38,855

The county with the largest voter turnout was Denver with 306,055 or 82.8%.  

## Winner of the Election
Ms. Diana Degette won the election by popular vote, after receiving 272,892 votes and 73.8% of the votes casts, which is above the 50.1% required by law.  
##  Summary
This analysis was completed using the Python coding language in the VS Code interpreter.  This code can be easily modified to support future election audits.  The code was puposfully written using repetitive statements.  The repetitive statements allow for the iteration of a CSV file with an unknown amount of rows and candidates. 
The code could be modified to accomodate a percentage to two decimal places by slightly altering these two code lines *f"Winning Percentage: {winning_percentage:**.1f**}%\n", f"{candidate_name}: {vote_percentage:**.1f**}% ({votes:,})\n")* -- change the .1f to .2f. 
Additionally, any of the variable names such as *candidate_options* can be changed, provided they are changed throughout the code.  
Please be aware that a CSV file might have a different column order that stores the name of the candidates and the vote count.  This is important because the Python code used for this analysis incorporated "indexing" to select the appropriate column.  For example, in Excel the columns are labeled A, B, C, etc.  In Python the first column "A" is 0, the second column "B" is 1, and so on.  I would be happy to assist with any future election audits.  
