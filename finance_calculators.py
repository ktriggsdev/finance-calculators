# imports the math module
import math

#Kumar, B. (2020) Python print 2 decimal places [%.2f in python], 
# Python Guides. Available at: https://pythonguides.com/python-print-2-decimal-places/ 
# (Accessed: March 20, 2023). 
# I wasn't completely sure how to format strings to 2 decimal places so I looked it up.

# the variable "finance_choice" takes input from the user (either 'investment' or 'bond')
finance_choice = input("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n \nEnter either 'investment' or 'bond' from the menu above to proceed: ")

# the value of the variable "finance_choice" is converted to all lowercase
finance_choice = finance_choice.lower()

# if the value of the "finance_choice" variable is equal to 'investment' or 'bond':
# the next if statement code block is run.
if (finance_choice == 'investment') or (finance_choice == 'bond'):
    
    # if the "finance_choice" variable is equal to 'investment':
    # "deposit_amount" variable takes input from the user: (please enter deposit amount:) and is cast to a integer value.
    if finance_choice == 'investment':
        deposit_amount = int(input("Please enter the deposit amount: "))
        
        # "interest_rate" variable takes input from the user: (please enter only the number of the interest rate:) and is cast to a integer value.
        interest_rate = int(input("Please enter only the number of the interest rate: "))
        
        # "interest_rate" is cast to a float value
        interest_rate = float(interest_rate)
        
        # "number_of_years" variable takes input from the user: (please enter the number of years you plan on investing: )
        number_of_years = int(input("Please enter the number of years you plan on investing: "))
        
        # "simple_compound" variable takes input from the user: (Please enter either 'simple' or 'compound' based on your preference: )
        simple_compound = input("Please enter either 'simple' or 'compound' based on your preference: ")
        
        # "simple_compound" variable is converted to all lowercase
        simple_compound = simple_compound.lower()
        
        # if "simple_compound" variable is equal to 'simple' then:
        # deposit_amount * (1 + interest_rate / 100 * number_of_years) is assigned to the "total_amount" variable
        if simple_compound == 'simple':
            total_amount = deposit_amount * (1 + interest_rate / 100 * number_of_years)
            
            # "total_amount" is then formatted to 2 decimal places as it is working with currency
            formatted_amount = "{:.2f}".format(total_amount)
            
            # the "formatted_amount" value is now displayed in the console.
            print(f"£{formatted_amount}")
            
        #the else if statement is called: if "simple_compound" is equal to 'compound' then:
        # deposit_amount * math.pow() module (1 + interest_rate / 100), number_of_years is assigned to the variable "total_amount"
        elif simple_compound == 'compound':
            total_amount = deposit_amount * math.pow((1 + interest_rate / 100), number_of_years)
            
            # total_amount is then formatted to 2 decimal places as it is working with currency
            formatted_amount = "{:.2f}".format(total_amount)
            print(f"£{formatted_amount}")
            
    #if none of the statements are matching, the else statement is called:
    # the user is asked to input the value_of_house (int) 
    else:
        value_of_house = int(input("Please enter the present value of the house (e.g. 100000): "))
        
        # the user is asked to input the interest_rate (int) 
        interest_rate = int(input("Please enter the interest rate (e.g. 7): "))
        
        # the user is asked to input the number_of_months planned to repay the bond (int) 
        number_of_months = int(input("Please enter the number of months that you plan to repay the bond (e.g. 120): "))
        
        # the (interest_rate variable / 100 / 12 * value_of_house variable)/(1 - (1 + interest_rate variable / 100 / 12)**(-number_of_months variable))
        # is assigned to the variable "repayment"
        repayment = (interest_rate / 100 / 12 * value_of_house)/(1 - (1 + interest_rate / 100 / 12)**(-number_of_months))
        
        # the "repayment" value is then formatted to 2 decimal places and assigned to the variable "formatted_repayment" as it is working with currency.
        formatted_repayment = "{:.2f}".format(repayment)
        
        # the "formatted_repayment" value is now displayed in the console.
        print(f"£{formatted_repayment}")
        
# if no statements above match then the else statement is called and an error will be displayed.
else:
    print("Error: You have entered an incorrect option, please only enter 'investment' or 'bond'!")
    
    