import re
password = "ak76d@#"
if re.match(r'^(?=.*?[0-9].*?[0-9])(?=.*[!@/#].*[!@/#])[0-9a-zA-Z!@#$%/0-9]{7,}$', password):
   	print("valid")
else:
	print('no valid')



# (?=.*?[0-9].*?[0-9]) #find at least two digits. Expression will fail if not.

# (?=.*[!@#$%].*[!@#$%]) #find at least Two characters in bracket [].

# [0-9a-zA-Z!@#$%0-9]{8,} #Match at least 8 of the characters inside bracket [] to be successful.

# $ # Match end of line. 





