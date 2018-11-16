#PtI: String Processing Puzzles

#Reveres Function 
def reverse(s):
	reverse_text = s[len(s):: -1]
	return reverse_text


#Test

print(reverse('blackbird'))                     


#Every Other Function 
def every_other(s):
	every_other_text = s[:len(s):2]
	return every_other_text

#Test
print(every_other('blackbird'))



#Outside Characters Function
def outside_chars(s,n):
	outside_chars_text = s[0:n]
	return outside_chars_texttouc

#Test
print(outside_chars('blackbird',3))


#Tripple Outside Function
def tripple_outsides(s):
	tripple_outside_text = s[0:2] * 3 + s[3:]
	return tripple_outside_text

#Test
print(tripple_outsides('blackbird'))


#Swap Halves Functino
def swap_halves(s):
	if len(s) % 2 == 0:
		swap_halves_text = s[len(s)/2:] + s[: len(s)/2-1]   
		return swap_halves_text
	else:
		swap_halves_text = s[int(round(len(s)/2)):] + s[:int(round(len(s)/2-1)):]
		return swap_halves_text

#Test
print(swap_halves('Good day sunshine '))


#Slice Middle Function 
def slice_middle(s):
	quarter = int(round(len(s)/4))
	minus_one = quarter - 1
	slice_middle_text = s[quarter: len(s)-quarter]
	return slice_middle_text

#Test
print(slice_middle("she came in through the bathroom window!"))





