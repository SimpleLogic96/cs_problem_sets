#Pt II: Simple Clock

#Time formatter
def format_time(current_hour, current_min):
	#if current minute is greater than 60
	if(current_min > 60):
		current_hour += 1
		current_min = current_min - 60

	#if current minute is equal to 60
	elif(current_min == 60):
		current_hour += 1
		current_min = 0

	#if current minute is within valid range
	else:
		current_hour = current_hour
		current_min = current_min 

		#if current hour is one digit long
		if(int(current_hour) <= 9):

			#if current minute is one digit long
			if(int(current_min) <= 9):
				formatted_time = '0' + str(current_hour) + ':' + '0' + str(current_min)
				return formatted_time

			#if current minute is two digits long
			else: 
				formatted_time = '0' + str(current_hour) + ':' + str(current_min)
				return formatted_time

		#if current hour is two digit long
		elif(int(current_hour) > 9):

			#if current minute is one digit long
			if(current_min <= 9):
				formatted_time = str(current_hour) + ':' + '0' + str(current_min)
				return formatted_time

			#if current minute is two digit long
			else:
				formatted_time =  str(current_hour) + ':' + str(current_min)
				return formatted_time



#Print out intervals of hours and minutes within a specified period of time
def print_times(start_hour, stop_hour, increment):
	#if start hour is greater than 24
	if(start_hour > 24):
		print('Error, your start hour is greater than 24!')

	#if stop hour is greater than 24
	elif(stop_hour > 24):
		print('Error, your stop hour is greater than 24!')

	#if the increment is not a factor of 60	
	elif(60 % increment != 0):
		print('Error, your increment is not a factor of 60!')

	#if the start and stop hours are within range and the increment is a factor of 60
	else:
		#Hour Loop
		for current_hour in range(start_hour, stop_hour + 1):
			#Minute Loop
			for min_times_counter in range(60//increment):
				#Add to current minute counter
				current_min = increment * min_times_counter

				#if current_hour exceeds the stop hour, print Time's Up! and break from loop
				if(current_hour > stop_hour and current_min != 0): 
					print('Times Up!')
					break

				#if current hour are equal and the current minute is 0, display the current hour with 0 as minutes
				elif(current_hour == stop_hour and current_min == 0):
					print(format_time(int(current_hour), 0))
					print('Times Up!')
				#if current_hour is within range, display the current time
				elif(current_hour < stop_hour):
					print(format_time(int(current_hour), current_min))	


start_hour = int(raw_input('Enter the start hour: '))
stop_hour = int(raw_input('Enter the stop hour: '))
increment = int(raw_input('Enter the increment: '))

print_times(start_hour, stop_hour, increment)

