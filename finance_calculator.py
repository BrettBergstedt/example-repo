import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you will have to pay on a home loan")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == "investment":
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == "simple":
        total_amount = principal * (1 + interest_rate * years)
    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    print(f"The total amount after {years} years will be: {total_amount:.2f}")
    deposit = float(input("The amount you deposited is: "))
    interest_rate = float(input("The interest rate is: ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))

    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()
    if interest_type == "simple":
        total_amount = deposit * (1 + interest_rate * years)
    elif interest_type == "compound":
        total_amount = deposit * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    print(f"The total amount after {years} years will be: {total_amount:.2f}")

elif choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    monthly_interest_rate = interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    print(f"The monthly repayment amount will be: {repayment:.2f}") 
    
else :
    print("Invalid choice. Please enter either 'investment' or 'bond'.")    