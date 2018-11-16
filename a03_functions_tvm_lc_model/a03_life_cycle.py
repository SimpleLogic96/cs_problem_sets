from a03_tvm import*


# Life Cycle Function (No I/O)
def life_cycle_model():
	c_age = float(raw_input("Enter your current age: "))
	r_age = float(raw_input("Enter your retirement age: "))
	int_rate = float(raw_input("Enter current interest rate:"))
	c_income = float(raw_input("Enter your current income: "))
	c_assets = float(raw_input("Enter your current assets: "))

	work_years = r_age - c_age
	h_capital = present_value_of_annuity(int_rate , work_years, c_income)
	e_net_worth = h_capital + c_assets
	years_of_consumption = 100 - c_age
	sus_living = annuity_payment(int_rate, years_of_consumption, c_assets)

	print("You have: " + str(work_years) + " left of working years.")
	print("Your anual income per year is: " + dollar_format(c_income) + " per year.")
	print("Your Human Capital is: " + dollar_format(h_capital) + ".")
	print("Your economic net worth is: " + dollar_format(e_net_worth) + "per year.")
	print("Your sustainable standard of living is about " + str(sus_living) + " per year.")



life_cycle_model()
