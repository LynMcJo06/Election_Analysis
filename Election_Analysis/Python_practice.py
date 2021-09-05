print("Hello World")
print("----------------")
print(5+ 2*3)
print(8//5-3)
print(8+22*2-4)
print(16-3/2+7-1)
print(3**3%5)
print(5+9*3/2-4)
print("---------------")
print("skill drill")
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / 2 - 4))
print(5 + (9 * 3/(2-4)))
print("--------------")
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
print(counties[-2])
print(len(counties))
print(counties[0:2])
print (counties[0:3])
print(counties[2:3])
print(counties[1:2])
print(counties[0:3])
print(counties[1:3])
print(counties[1:])
print(counties.append("El Paso"))
print(counties)
print(counties.insert(2, "El Paso"))
print(counties)

print("------------------")
print(counties.remove("El Paso"))
print(counties)
print("incorrect--------next try")
counties.insert(2, "El Paso")
print(counties)
print("Attempting to get list back to 5 counties")
print(counties)
print("After several attempts to fix my error, I erased the line of code that created the error")
print(counties)
counties.remove("El Paso")
print(counties)
print(counties[0:1])
print(counties[0:2])
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties.pop(-1)
print(counties)
counties.append("El Paso")
print(counties)
counties.append("Jefferson")
print(counties)
counties.pop(2)
print(counties)
counties[2] = "El Paso"
print(counties)
counties[2] = "Jefferson"
print(counties)
counties.insert(1, "El Paso")
print(counties)
counties.remove("Arapahoe")
counties.insert(2, "Denver")
counties[1] = "Jefferson"
counties.pop(3)
counties.append("Arapahoe")
print(counties)


print("-------------------")
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])

print("----------------")
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)


print("----New Exercise----")
print("-----Add new county El Paso and its registered voters to the second position-----")
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
print(voting_data)


print("----Remove Arapahoe and its registered voters-------")
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)


print('--Make Denver and voters the third item and keep Jefferson and voters as second item-----')
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
print(voting_data)

print("----Add Arapahoe and its voters------")
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
print(voting_data)

print("----If Statements Exercise----")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

print("----If - Else Statements Exercise----")
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

print("---Nested if-else statements practice----")
#What is the score?
score = int(input("What is your test score?"))

#Determine the grade. 
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print("your grade is a D.")
            else:
                print('Your grade is an F and you fail.')

print('---if-elif-else statements practice----')
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F and you fail.')

print("----Membership Operators Exercise")
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
 
print('------------------')  
print('Create a compound membership and logical operation.')
if "Arapahoe" in counties and "El Paso" in counties:
     print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")  

print('----------------')
## Use a compound expression to determine if either county is in the list.
if "Arapahoe" in counties or "El Paso" in counties:
    print('Arapahoe or El Paso is in the list of counties.')
else: 
    print('Arapahoe and El Paso are not in the list of counties.')

print('--------------')
## Repetitive Statements (Loops)
for county in counties:
    print (county)

print('---------------')
## Skill Drill:  Print each county from the "counties" dictionary
##  using the keys() method. 
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

print('----------')
for county in counties_dict:
    print(counties_dict[county])

print('---------')
## Get key-value pairs.
for county, voters in counties_dict.items():
    print(county, voters)

print('----------')
## Skill Drill:  Print county registered voters in specific form.
for county, voters in counties_dict.items():
    print(county + ' county has ' + str(voters) + ' registered voters.')

print('-----------')
## Get each dictionary in a list of dictionaries.
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
print('----------')
## Get the values from the list of dictionaries.
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
print('----------')
## Use multiple f-strings to print.
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
print('-----------')
## Reformat the above code to add a thousands separator and percentage to two decimal places.
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
print('-----------')
## Skill Drill:  Print each county and registered voter from the dictionary. 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

print('----------')
## Skill Drill:  Print each county and registered voter from the dictionary.
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]
for data in voting_data:  
    print(f"{data['county']} county has {data.get('registered_voters'):,} registered voters.")

