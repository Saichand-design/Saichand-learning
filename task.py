# Mahindra Scorpio N EMI Calculator (Basic Script)

# Step 1: Set basic inputs
on_road_price = 1726297   # in ₹
down_payment = 200000     # in ₹
loan_amount = on_road_price - down_payment  # ₹15,26,297
interest_rate = 10        # Annual interest rate in %
loan_period_years = 5     # 5 years

# Step 2: Convert years to months
loan_period_months = loan_period_years * 12

# Step 3: Calculate monthly interest rate
monthly_interest_rate = interest_rate / (12 * 100)  # 10% annually → ~0.0083 monthly

# Step 4: Calculate EMI using basic formula
numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_period_months
denominator = (1 + monthly_interest_rate) ** loan_period_months - 1
emi_per_month = numerator / denominator

# Step 5: Calculate total payable amount
total_payable = emi_per_month * loan_period_months

# Step 6: Print results
print("Mahindra Scorpio N EMI Details:")
print("On-Road Price       : ₹", on_road_price)
print("Down Payment        : ₹", down_payment)
print("Loan Amount         : ₹", loan_amount)
print("Interest Rate       :", interest_rate, "% per annum")
print("Loan Period         :", loan_period_years, "years")
print("Monthly EMI         : ₹", int(emi_per_month))
print("Total Payable Amount: ₹", int(total_payable))
