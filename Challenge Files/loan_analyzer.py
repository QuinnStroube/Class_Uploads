# # coding: utf-8
import csv
from dataclasses import dataclass
from pathlib import Path

# # """Part 1: Automate the Calculations.

# # Automate the calculations for the loan portfolio summaries.

# # First, let's start with some calculations on a list of prices for 5 loans.
# #     1. Use the `len` function to calculate the total number of loans in the list.
# #     2. Use the `sum` function to calculate the total of all loans in the list.
# #     3. Using the sum of all loans and the total number of loans, calculate the average loan price.
# #     4. Print all calculations with descriptive messages.
# # """
loan_costs = [500, 600, 200, 1000, 450]

# # # How many loans are in the list?
# # # @TODO: Use the `len` function to calculate the total number of loans in the list.
# # # Print the number of loans from the list
# # # YOUR CODE HERE!

len(loan_costs)                                                                 #Calculate number of loans in list
print("There are",len(loan_costs),"loans in the list.")                         #Print number of loans in list

# # # What is the total of all loans?
# # # @TODO: Use the `sum` function to calculate the total of all loans in the list.
# # # Print the total value of the loans
# # # YOUR CODE HERE!

def sum_of_loans(loan_amount):                                                  #Define the function to sum the loans
    loan_totals = sum(loan_amount)                                              #Create a variable for total of loans using sum function
    
    return loan_totals                                                          #Return the value of the loans

total_loan_amount = sum_of_loans(loan_costs)                                    #ASK ABOUT THIS
print(f"The total of all the loans is ${total_loan_amount: .2f}")               #Print total loan amount using f string rounded to 2 decimals


# # # What is the average loan amount from the list?
# # # @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# # # Print the average loan amount
# # # YOUR CODE HERE!

def average_loan(loan_amount):                                                  #Define the function to get the average loan amount
    average = total_loan_amount/len(loan_costs)                                 #Create a variable to calculate average loan amount

    return average                                                              #Return the average of the loans
loan_average = average_loan(loan_costs)                                         #Call the function to calculate the average of the loan cost list
print(f"The average loan amount is ${loan_average: .2f}")                       #Print f-string for the average loan amount

# """Part 2: Analyze Loan Data.

# Analyze the loan to determine the investment evaluation.

# Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

# 1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
#     a. Save these values as variables called `future_value` and `remaining_months`.
#     b. Print each variable.

#     @NOTE:
#     **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
#     **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

# 2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
# 3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#     a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#     b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

#     @NOTE:
#     If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
# """

# # Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# # @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# # Print each variable.
# # YOUR CODE HERE!

loan.get("future_value")                                                            #Retrieve future value from dictionary
loan.get("remaining_months")                                                        #Retrieve remaining months from dictionary

print("The future value of the loan is",loan.get("future_value"))                   #Print future value of the loan
print("There are",loan.get("remaining_months"),"months remaining on the loan")      #Print the months remaining on the loan

# # @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# # Use a minimum required return of 20% as the discount rate.
# #   You'll want to use the **monthly** version of the present value formula.
# #   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# # YOUR CODE HERE!

def pv_of_loan(future_value, remaining_months):                                     #Define the present value function
    present_value = future_value / (1 + .20/12) ** remaining_months                 #Create a variable to calculate the present value of the loan
    #print("pv",present_value)                                                      #Optional print statement to check calculations
    return present_value

present_value_loan = pv_of_loan(loan["future_value"],loan["remaining_months"])      #Call the present value function to calculate the present value of the loan
print(f"The fair value of the loan is ${present_value_loan: .2f}")                  #Print f-string to print fair value rounded to 2 decimals

# # If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# # @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
# #    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
# #    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# # YOUR CODE HERE!

if present_value_loan >= loan.get("loan_price"):                                    #If condition to test whether the present value is more than the loan
    print("The loan is worth at least the cost to buy it.")                         #Print statement if the loan is worth it
else:                                                                               #Else condition to test if present value is less than the loan price
    print("The loan is too expensive and not worth the price.")                     #Print statement if the loan is not worth it

# """Part 3: Perform Financial Calculations.

# Perform financial calculations using functions.

# 1. Define a new function that will be used to calculate present value.
#     a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#     b. The function should return the `present_value` for the loan.
# 2. Use the function to calculate the present value of the new loan given below.
#     a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# """

# # Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# # @TODO: Define a new function that will be used to calculate present value.
# #    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# #    The function should return the `present_value` for the loan.
# # YOUR CODE HERE!

def calculate_present_value(future_value,remaining_months,annual_discount_rate):                    #Define the function to calculate pv using the three parameters
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months                #Create variable to calculate pv
    #print("PV",present_value)                                                                      #Optional print to check calculation
    return present_value                                                                            #Return function which returns the calculated pv


# # @TODO: Use the function to calculate the present value of the new loan given below.
# #    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# # YOUR CODE HERE!

new_loan["annual_discount_rate"] = .2
pv_loan = calculate_present_value(new_loan["future_value"],new_loan["remaining_months"],new_loan["annual_discount_rate"])
print()
print(f"The present value of the loan is: ${pv_loan: .2f}")
print()
# """Part 4: Conditionally filter lists of loans.

# In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

# 1. Create a new, empty list called `inexpensive_loans`.
# 2. Use a for loop to select each loan from a list of loans.
#     a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
#     b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
# 3. Print the list of inexpensive_loans.
# """

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# # @TODO: Create an empty list called `inexpensive_loans`
# # YOUR CODE HERE!

inexpensive_loans = []

# # @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# # YOUR CODE HERE!

for loan_amount in loans:
    if loan_amount["loan_price"] <= 500:
        inexpensive_loans.append(loan_amount)
print(inexpensive_loans)

# for loan_amount in loans[:]:
#     loan_price = loan_amount.get("loan_price")
#     loan_months = loan_amount.get("remaining_months")
#     loan_repayment = loan_amount.get("repayment_interval")
#     future_value = loan_amount.get("future_value")
#     if loan_price <= 500:  
#         inexpensive_loans.append(loan_price)
#         inexpensive_loans.append(loan_months)
#         inexpensive_loans.append(loan_repayment)
#         inexpensive_loans.append(future_value)

# # @TODO: Print the `inexpensive_loans` list
# # YOUR CODE HERE!

print(f"Here is a list of inexpensive loans {inexpensive_loans}")

# """Part 5: Save the results.

# Output this list of inexpensive loans to a csv file
#     1. Use `with open` to open a new CSV file.
#         a. Create a `csvwriter` using the `csv` library.
#         b. Use the new csvwriter to write the header variable as the first row.
#         c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#             i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

#     Hint: Refer to the official documentation for the csv library.
#     https://docs.python.org/3/library/csv.html#writer-objects

# """

# # Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# # Set the output file path
output_path = Path("inexpensive_loans.csv")

# # @TODO: Use the csv library and `csv.writer` to write the header row
# # and each row of `loan.values()` from the `inexpensive_loans` list.
# # YOUR CODE HERE!
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # for row in inexpensive_loans:
    csvwriter.writerow(header)
    for loans in inexpensive_loans:
        csvwriter.writerow(loans.values())
