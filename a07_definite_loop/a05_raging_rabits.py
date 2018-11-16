import math
import random

#Opening text
print("Welcome to Raging Rabits!")

#Function to compute distance (D)
def calculate_projectile_distance(launch_angle, initial_velocity):
	distance = (initial_velocity ** 2  / 9.8) * (math.sin(2 * math.radians(launch_angle)))
	return distance

#Function to calculate luanch angle (l_angle)
def calculate_launch_angle(distance, initial_velocity):
	l_angle = 0.5 * math.asin(9.8 * distance / int(initial_velocity) ** 2)
	return math.degrees(l_angle)


#Raging Rabits Function 
def raging_rabits():

	#User input velocity
	launch_velocity = raw_input("Enter the desired launch velocity (in m/s): ")

	#Defining max distance, min distance, and random distance
	min_distance = int(calculate_projectile_distance(10, int(launch_velocity)))
	max_distance = int(calculate_projectile_distance(45, int(launch_velocity)))
	random_distance = random.randint(min_distance, max_distance)

	#Display min and max distance, and location of target to user
	print("With an initial launch velocity of " + str(launch_velocity) +
	 " m/s, your cannon can hit a target between " + str(min_distance) + " and " + str(max_distance) + " meters.")
	print("Your target is located at " + str(random_distance) + "meters.")

	#User launch angle input from user and calculations
	user_launch_angle = raw_input("Enter your launch angle (in degrees): ")
	distance_traveled = int(calculate_projectile_distance(float(user_launch_angle), float(launch_velocity)))
	difference_in_distance = distance_traveled - random_distance 

	#Display distance traveled and difference between distance traveld and distance to the target
	print("Your projectile traveled " + str(distance_traveled) + " meters.")

	if (difference_in_distance > 0):
		print("You overshot by " + str(difference_in_distance) + " meters, try again")
		return 

	else:
		print("You undershot by " + str(difference_in_distance) + " meters, try again")
		return



#raging_rabits()

# print(calculate_projectile_distance(25, 50))
# print(calculate_launch_angle(250, 50))

#print(calculate_projectile_distance(0, 196))