#[9:06 PM, 1/30/2020] Ashu Yo Yo: New Driver's License +100 XP

# You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

# Task 
# Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

# Input Format 
# Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

# Output Format 
# You will output an integer of the number of minutes that it will take to get your license.

# Sample Input
# 'Eric'
# 2
# 'Adam Caroline Rebecca Frank'

# Sample Output 
# 40


name = 'Zebediah'
agents = 1
other_name = 'Bob jim Becky Pat'

persons = other_name.split(' ')
persons.append(name)
persons.sort()
position = persons.index(name)
output = 0

for person in persons:
	if(agents == 1):
		output+=20
		if(person != name):
			pass
		else:
			break

	if(agents == 2):
		output+=20
		if(person != name):
			pass
		else:
			break



print(output)





























