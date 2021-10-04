# Tip Calculator Project: "The Biltipulator"

# The tip calculator will output or print its brand name.

print('Thank you for using the Biltipulator')
print()

# The tip calculator will output or print a well wish.

print('Hope you enjoyed your meal!')
print()

# The variable "bill" is assigned a string that will output or print "Enter the total bill" to the terminal
# and will convert the customer input of the total bill amount to the form of a float or decimal number.

# The tip calculator asks the customer to input the total bill amount.

bill = float(input('Enter the total bill: '))

# The variable "tip" is assigned a string that will output or print "Enter tip %" 
# to the terminal and convert the customer input the tip percentage amount to the integer number format. 

# The tip calculator will ask the customer to input the tip percentage amount.

tip = int(input('Enter tip %: '))

# The variable "split_bill" is assigned a string that will output or print "How many people are splitting the bill"
# to the terminal and accept the customer input number of people splitting the bill as an integer.

# The tip calculator will ask the customer to input the number of how many people are splitting the bill.

split_bill = int(input('How many people splitting the bill?: '))

# The variable "payments" will output the amount that each person will pay, based on the tip percentage,
# multiplied by the total bill, and divided by the total number of people entered by the customer.

# The tip calculator will then calculate the amount each person will pay, including tip amount.

payments = (round(float(((tip/100 + 1)* bill)/split_bill), 2))
print(f'Payment for each: ${payments}')