# #Task 1 Collecting User Details
# name = input("Please input your name: ")
# age = int(input("Please input your age: "))
# print(f"Hello {name}, you are {age} years old.")
# #Task 2 Price Display with Type Casting
# price = float(input("Please input the price of garri per paint in nair: "))
# print(f"The price of garri per paint is ₦{float(price)}kobo.")

# #Task 3 School Registration Form
# name = input("Please input your name: ")
# SClass = input("Please input your class: ")
# StateOfOrigin = input("Please input your state of origin: ")
# print("Your name is " + name + ", you are in class " + SClass + ", and your state of origin is " + StateOfOrigin + ".")

# #Task 4 Escape Sequence
# food = input("Please input your favorite Nigerian food: ")
# state = input("Please input the state known for that food: ")
# print(f"The name of your favorite Nigerian food is {food}, \nand it is known in \t{state} state.")

# #Task 5 Daily Market Report
# market = input("Please input the name of the market: ")
# traders = int(input("Please input the number of traders in the market: "))
# revenue = float(input("Please input the total revenue generated in the market: "))
# #using comma for thousands separator
# print(f"The name of the market is {market}, there are {traders} traders, the total revenue generated is ₦{revenue:,}kobo.")

# #Task 6 Electricity Bill Formatter
# name = input("Please input your full name: ")
# UnitConsumed = int(input("Please input the number of units consumed in kWh: "))
# cost = float(input("Include the cost of electricity per unit: "))

# bill = float(cost*UnitConsumed )
# print(f"Hello {name} \n\t\tYour light bill is as follows \nUnits consumed in kWh:\t{UnitConsumed} \
# \tCost per unit:\t{cost} \nYour total bill is: ₦{bill}kobo")

# #Task 7 Mixing Data Types
# age = int(input("Please input your age: "))
# height = float(input("Please input your height in meters: "))
# name = input("Please input your name: ")
# print(f"Your name is {name}, you are {str(age)} years old, and your height in meters is {str(height)}.")

# #Task 8 Transport Fare Calculator
# distance = float(input("Please input the distance in km: "))
# fare = float(input("Please input the fare per km: "))
# TotalFare = float(distance*fare)
# print(f"Your total fare for {distance}km is {TotalFare:.2f}")

# #Task 9 Nigerian Festival Info
# FestivalName = input("Please input the name of the festival: ")
# location = input("Please input the location of the festival: ")
# month = input("Please input the month in which the festival held: ")
# print(f'\"The {FestivalName} festival held at {location} in the month of {month}.\"')

# #Task 10 School Fees Breakdown
# name = input("Please input the name of the school: ")
# tution = float(input("Please input the tution fee: "))
# HostelFee = float(input("Please input the hostel fee: "))
# FeedingFee = float(input("Please input the feeding fee: "))
# total = float(tution*HostelFee*FeedingFee)
# print(f"\t\t\tFees breakdown for {name} \nTution fee: {tution} \nHostel Fee: {HostelFee}\
# \nFeeding fee: {FeedingFee} \nTotal: ₦{str(total)}kobo")

#Task 11 Nigerian Currency Converter 
amount = float(input("Please input the amount to be converted in naira: "))
dollars = float(input("Please input the exchange rate from naira to US Dollars: "))
pounds = float(input("Please input the exchange rate from naira to British pounds: "))
ConvertedDollars = float(amount*dollars)
ConvertedPounds = float(amount*pounds)
print(f"Amount in naira(₦) \tAmount in US Dollars($) \tAmount in British Pounds(£) \n{amount:,} \t\t{ConvertedDollars:,} \t\t\t{ConvertedPounds:,}")

#Task 13 Simulated USSD Menu Interacation
