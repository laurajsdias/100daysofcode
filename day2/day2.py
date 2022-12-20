# Day 2 - Data types and mathematical operations

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tip_perc = int(tip) / 100
tip_value = tip_perc * float(bill)
total_bill = tip_value + float(bill)

split_value = round(total_bill / int(num_people))

print(f"Each person should pay: ${split_value}")