from a05_raging_rabits import *

#Generate random integer between 100 and 200 for set initial velocity

#initial_velocity = random.randint(100,200)
random_velocity = 196

print('Your cannon has been calibrated with an initial launch velocity of ' + str(random_velocity) + 'm/s.')

#Function to find greatest distance within range

def find_greatest_distance(distance_list):
	greatest_distance = distance_list[0]

	for distance in range(0,90):
		if (greatest_distance >= distance_list[int(distance) + 1]):
			print(str(greatest_distance) + '>=' + str(distance_list[int(distance)]))
			greatest_distance = greatest_distance
			print(greatest_distance)

		elif (greatest_distance < distance_list[int(distance)]):
			print(str(greatest_distance) + '<=' + str(distance_list[int(distance)]))
			greatest_distance = distance_list[int(distance)]
			print(greatest_distance)

		return greatest_distance

#Function to find the smallest distance within range

def find_least_distance(distance_list):
	least_distance = distance_list[0]

	for distance in range(0, 90):
		if(least_distance <= distance_list[int(distance)]):
			least_distance = least_distance 

		elif(least_distance > distance_list[int(distance)]):
			least_distance = distance_list[int(distance)]

		else:
			break

		return least_distance




#Calculate the range of distance the projectile can travel given initial veloicty using for loop
def calculate_range_distance():
	distance_list = []
	for angle in range(0,90):
		distance = calculate_projectile_distance(angle, random_velocity)
		distance_list = distance_list + [distance]


	#print(distance_list)
	find_greatest_distance(distance_list)
	#print(find_least_distance(distance_list))



calculate_range_distance()

#print('At this velocity, you can hit a target between ' + str(min_distance) + ' and ' + str(max_distance) + ' meters.')


