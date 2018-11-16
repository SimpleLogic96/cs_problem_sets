#Pt I: Finding the Minimum of 3 Numbers
#No built in functions and no input functions

#function to find minimum number of 2 Numbers

def my_min(a,b):
	if a > b:
		return b
	else:
		return a


#Tests
#print('my_min(1,2)', my_min(1,2))
#print('my_min(2,1)', my_min(2,1))

#Function to find min number out of 3 parameters

def find_min(a, b, c):
	d = my_min(a,b)
	d_c_min = my_min(d, c)
	return d_c_min



#Test Case
if __name__ == '__main__':
	print('find_min(1,2,3)', find_min(1,2,3))
	print('find_min(2,1,3)', find_min(2,1,3))
	print('find_min(3,2,1)', find_min(3,2,1))




