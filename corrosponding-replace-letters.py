import string
s = "Vegetable pizza"
# taking all the ascii characters form a to z 
letters = string.ascii_lowercase
#creating dictionary for each letter like { 'a':'z','b':'y','c':x'........}
reverse_letters = dict(zip(letters,letters[::-1]))

#
#first method to get the value

# ai = ''.join(map(reverse_letters.get,s.replace("","").lower()))

#second method to get the value
def get_reverse_value(letters):
	letters = letters.lower()
	return reverse_letters[letters]

ai = ''

for letter in s:
	if(letter == ' '):
		ai += " "
	else:
		ai += get_reverse_value(letter)


# Print the final answer
print(ai)
	





