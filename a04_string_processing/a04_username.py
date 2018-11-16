#Pt II: String Processing Puzzles

#Username Function
def username (first, middle, last):
	username = first[0] + middle[0] + last[:7]
	return username


#I/O and Call function 
first = raw_input("What is your first name?")
middle = raw_input("What is your middle name?")
last = raw_input("what is your last name?")
print(username (first, middle, last))

