#Pt II: Validating Data Input
#No User input

#Determine if month value is Valid
def is_valid_month(month):
	if(month > 12):
		return False
	elif(month <= 0):
		return False
	else:
		return True

#Test Cases:
#print(is_valid_month(5))
#print(is_valid_month(-5))
#print(is_valid_month(13))

#Determine if year value is a leap year
def is_leap_year(year):
	if(year % 4 != 0):
		return False
	elif(str(year)[2:4] == '00' and year % 400 != 0):
		return False
	else:
		return True


#Test Cases:
#print(is_leap_year(2012))
#print(is_leap_year(2016))
#print(is_leap_year(2011))
#print(is_leap_year(2200))
#print(is_leap_year(1937))	


#Determine if the input day value is within the number of days of the input month
def is_valid_day_in_month(month, day, year):
	if(is_valid_month == False):
		return False
	elif(day <= 0):
		return False
	else:	

		if(month == 1 or month ==  3 or month ==  5 or month ==  7 or month ==  8 or month ==  10 or month ==  12):
			if(day > 31):
				return False
			else:
				return True

		elif(month == 4 or month ==  6 or month ==  9 or month == 11):
			if(day > 30):
				return False
			else:
				return True

		elif(month == 2):
			if(is_leap_year(year) == True and day > 29):
				return False
			elif(is_leap_year(year) != True and day > 28):
				return False
			else: 
				return True




#Test Cases
"""
print(is_valid_day_in_month(1, 5, 1920), is_valid_day_in_month(4, 5, 1920), is_valid_day_in_month(2, 5, 1920))
print(is_valid_day_in_month(3, -5, 1920), is_valid_day_in_month(6, -5, 1920), is_valid_day_in_month(2, -5, 1920))
print(is_valid_day_in_month(5, 35, 1920), is_valid_day_in_month(9, 35, 1920), is_valid_day_in_month(2, 35, 1920))
print(is_valid_day_in_month(7, 31, 1920), is_valid_day_in_month(11, 31, 1920), is_valid_day_in_month(2, 31, 1920))
print(is_valid_day_in_month(2, 29, 1921), is_valid_day_in_month(2, 29, 1921), is_valid_day_in_month(2, 29, 1921), is_valid_day_in_month(2, 29, 2012))
"""

#Function to return integer value of month to string
def get_month_name(month):
	name_array = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	return name_array[int(month) - 1]

#Test Cases
#print(get_month_name(1))
#print(get_month_name(5))

#Check if input date is valid 
def is_valid_date(month, day, year):
	if(is_valid_day_in_month(month, day, year) == False):
		month_name = get_month_name(month)
		print(str(month) + "/" + str(day) + "/" + str(year) + " is not a valid date, because day " + str(day) + " is not a valid date for " + month_name + ", " + str(year) + ".")
	elif(is_valid_month(month) == False):
		print(str(month) + "/" + str(day) + "/" + str(year) + " is not a valid date because " + str(month) + " is not a valid month")
	else:
		month_name = get_month_name(month)
		print(str(month) + "/" + str(day) + "/" + str(year) + " is a valid date.")
				


#Test Case for is valid date function
is_valid_date(02,29,2016)
is_valid_date(02,29,2017)
is_valid_date(02,29,2018)
is_valid_date(01,32,2018)
is_valid_date(13,07,2016)


