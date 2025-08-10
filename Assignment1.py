#Task 5 Daily Market Report

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

#Task 10 School Fees Breakdown
name = input("Please input the name of the school: ")
tution = float(input("Please input the tution fee: "))
HostelFee = float(input("Please input the hostel fee: "))
FeedingFee = float(input("Please input the feeding fee: "))
total = float(tution*HostelFee*FeedingFee)
print(f"\t\t\tFees breakdown for {name} \nTution fee: {tution} \nHostel Fee: {HostelFee}\
\nFeeding fee: {FeedingFee} \nTotal: ₦{str(total)}kobo")

#Task 11 Nigerian Currency Converter 
amount = float(input("Please input the amount to be converted in naira: "))
dollars = float(input("Please input the exchange rate from naira to US Dollars: "))
pounds = float(input("Please input the exchange rate from naira to British pounds: "))
ConvertedDollars = float(amount*dollars)
ConvertedPounds = float(amount*pounds)
print(f"")
