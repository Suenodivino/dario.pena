# Tip Calculator Project: "The Biltipulator"

# The tip calculator will output or print its brand name.

print('Thank you for using the Biltipulator')

# The tip calculator will output or print a well wish.

print('Hope you enjoyed your meal!')
print()

# The variable "bill" is assigned a string that will output or print "Enter the total bill" to the terminal
# and will convert the customer input of the total bill amount to the form of a float or decimal number.

# The tip calculator asks the customer to input the total bill amount.

bill = float(input('Enter total bill: '))

# The variable "tip" is assigned a string that will output or print "Enter tip %" to the terminal and
# the customer input amount will be stored in integer number format. 

# The tip calculator will ask the customer to input the tip percentage amount.

tip = int(input('Enter tip%: '))

# The variable "tax" is assigned 10% of the total bill as a float to be added to the total cost of 
# the meal.

tax = (.10 * bill)

# The variable "split_bill" is assigned a string that will output or print "How many people are splitting the 
# bill?" to the terminal, and the customer input number of people splitting the bill as an integer.

# The tip calculator will ask the customer to input the number of how many people are splitting the bill.

split_bill = int(input('How many people splitting the bill?: '))

# The tip calculator will then calculate the amount each person will pay, by dividing the tip amount by 100 
# to get the amount for the tip, multiplied by the total bill, which resulting number is then divided by the
# number of people paying, and the 10% sales tax is added to the result.

# The variable "payments" will calculate the amount that each person will pay, based on the tip percentage 
# (which is divided by a hundred), multiplied by the total bill, and divided by the total number of people 
# entered by the customer, adding the 10% sales tax and dividing this by the number of people paying.

payments = (float(tip/100 + 1)* bill)/split_bill + tax/split_bill

# The variable "payments" will only add two numbers behind the decimal number, which will be a float.

payments = round(payments, 2)

# The print function will now output to the terminal the amount that each person will pay.
  
print(f'payment for each: ${payments}')