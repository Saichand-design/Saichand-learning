car_variant = "z2E pertol"
on_road_price = 2007695
loan_period_year = 5
rate_of_interest = 8
down_payment = 500000

#simple_interest = (car_price - initial_downp_payment)*rate_of_interest*time_period /100
#total_amout = car_price - initial_down_payment + simple_interest 
#monthly_installment = total_amount / (time_period *12)

#correct implementation 
loan_amount = on_road_price - down_payment
months = loan_period_year * 12
monthly_interest_rate = rate_of_interest / (12*100)

emi = (loan_amount * monthly_interest_rate*((1+monthly_interest_rate)**months))/ (((1+monthly_interest_rate)**months)- 1)

payable_amount = emi* months

print("====================================")
print(f"car variant: {car_variant}")
print(f"car price: {on_road_price}")
print(f"time period : {loan_period_year} years")
print(f"Rate of interest: {rate_of_interest}%")
print(f"intitial Down Payment : {down_payment}")

print(f"total amount payable: {payable_amount}")
print(f"monthly Installment: {emi}")