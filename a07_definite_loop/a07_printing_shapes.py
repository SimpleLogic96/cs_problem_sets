#Pt I: Printing Patterns with For Loop

print(' ')
#Rectangle
def print_rect(ch, width , height):
	for x in range(0, int(height)):
		print(ch * width)

#Rectangle test
print_rect('*', 7, 5)

print(' ')

#Upper left triangle
def print_upper_left_triangle(ch, height):
	for x in range(0, height):
		print(ch * height)
		height += -1
#Upper left triangle Ttst
print_upper_left_triangle('*', 5)

print(' ')

#Upper right triangle
def print_upper_right_triangle(ch, height):
	empty_char = ''
	for x in range(0, height):
		new_height = height - x
		print(empty_char + ch * int(new_height))
		empty_char += ' '
		

#Upper left triangle test
print_upper_right_triangle('*', 5)


#Lower left triangle:
def print_lower_left_triangle(ch, height):
	for x in range(0, height + 1):
		print(ch * x)


#Lower left triangle test:
print_lower_left_triangle('*', 5)

print(' ')

#Lower right triangle:
def print_lower_right_triangle(ch, height):
	new_height = height - 1
	for x in range(0, height + 1):
		print(' ' * new_height + ch * x)
		new_height = height - x
		new_height += 1

#Lower right triangle test:
print_lower_right_triangle('*', 5)

print(' ')

#Pyramid:
def print_pyramid(ch, height):
	empty_char = ' '
	total_num_of_stars = (height - 1) * 2 
	char_counter = 1

	for x in range(0, height):
		num_of_empty_char = (total_num_of_stars - char_counter) // 2 
		print(empty_char * int(num_of_empty_char + 1) + ch * int(char_counter))
		char_counter += 2
		
#Pyramid Test
print_pyramid('*', 5) 

print(' ')

#Diamond
def print_diamond(ch, height):
	print_pyramid(ch,int(height/2))
	empty_char = ' '
	total_num_of_stars = (height/2 - 1) * 2
	char_counter = total_num_of_stars - 1
	for x in range(1, height):
		num_of_empty_char = (total_num_of_stars - char_counter) // 2 
		print(empty_char * int(num_of_empty_char + 1) + ch * int(char_counter))
		char_counter += -2


#Diamond Test
print_diamond('*', 10)

print(' ')



