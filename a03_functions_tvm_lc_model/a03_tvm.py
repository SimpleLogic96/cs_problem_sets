#Pt I: Time Value of Money Calculations 

#Future Value Function
def future_value(rate, nper, pv):
	fv = pv * (1 + rate) ** nper
#	print("Your future value of your investments is: " + dollar_format(fv))
	return fv

#Present Value Function 
def present_value(rate, nper, fv):
	pv = fv / (1 + rate) ** nper
#	print("Your present value of your investment is: " + dollar_format(pv))
	return pv

#Present Value of Annuity Function 
def present_value_of_annuity(rate, nper, pmt):
	pva = (pmt * (1 - (1/(1 + rate) ** nper)) / rate) 
#	print("Your present value of annuity is: " + dollar_format(pva))
	return pva

#Annuity Payment Function 
def annuity_payment(rate, nper, pv):
	pmt = (rate * pv) / (1 - (1 + rate) ** -nper)
#	print("Your annuity payment is: " + dollar_format(pmt))
	return pmt

#Dollar Format Function 
def dollar_format(ammount):
	dollar_amm = "$" + str(round(ammount))
	return dollar_amm



#Test Feature 
'''
rate = float(raw_input("Enter Rate here: "))
nper = float(raw_input("Enter number of Periods here: "))
pv = float(raw_input("Enter present value here (if applicable): "))
fv = float(raw_input("Enter future value here (if applicable): "))
pmt = float(raw_input("Enter your Present value of annuity here: "))

future_value(rate, nper, pv)
present_value(rate, nper, fv)
present_value_of_annuity(rate, nper, pmt)
aunnuity_payment(rate, nper, pv)

'''