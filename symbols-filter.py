import string
default = "#l$e%ts go @an#d@@ g***et #l#unch$$$"

letters = string.ascii_lowercase

def get_letter_only(letter):
	if letter in letters:
		return letter


final = ''
for letter in default:
	if(letter == ' '):
		final += ' '
	elif get_letter_only(letter) != None:
		final += get_letter_only(letter)
	else:
		pass


print(final)