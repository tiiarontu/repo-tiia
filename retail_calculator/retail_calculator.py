'''
Created on 12.9.2023

@author: Helena and Tiia
'''
def count_total_price():

    #User inputs
    print("The program counts the total order price.\n")
    try:
        n_items = float(input("Insert the number of items\n"))
    except ValueError:
        raise ValueError("Please enter a valid number.")
    try:
        unit_price = float(input("Insert unit price\n"))
    except ValueError:
       raise ValueError("Please enter a valid number.")
    
    list_allowed_states = ["UT","NV", "TX", "AL", "CA"]
    state = "0"
    while state not in list_allowed_states:
        state = input("Insert state code\n")
        if state not in list_allowed_states:
            print("Enter valid state code.")

    #Find tax rate
    if state == "UT":
        tax_rate = 0.0685
    if state == "NV":
        tax_rate = 0.08
    if state == "TX":
        tax_rate = 0.0625
    if state == "AL":
        tax_rate = 0.04
    if state == "CA":
        tax_rate = 0.0825

    #Calculate total price before taxes and discounts
    total_price_ex_tax = n_items*unit_price
    #Calculate total amount of tax
    total_tax = total_price_ex_tax*tax_rate

    #Calculate discount rate
    if total_price_ex_tax >= 50000:
        discount_rate = 0.15
    elif total_price_ex_tax >= 10000:
        discount_rate = 0.10
    elif total_price_ex_tax >= 7000:
        discount_rate = 0.07
    elif total_price_ex_tax >= 5000:
        discount_rate = 0.052
    else:
        discount_rate = 0.03

    #Calculate discount amount
    total_discount = total_price_ex_tax*discount_rate

    #Calculate total price after taxes and discounts
    total_price = total_price_ex_tax + total_tax - total_discount

    #Print values
    print("\nThe number of items equals {:.0f} and the unit price equals {} dollars.". format(n_items, unit_price))
    print("\nThe total order price prior taxes and discounts equals {} dollars.". format(total_price_ex_tax))
    print("\nWith state {} tax rate equal to {:.2f}% and the total amount of tax equals {} dollars.". format(state, 100*tax_rate, total_tax))
    print("\nThe discount rate equals {:.2f}%.". format(100*discount_rate))
    print("\nThe total order price equals {} dollars.\n". format(total_price))

def main():
    count_total_price()
main()