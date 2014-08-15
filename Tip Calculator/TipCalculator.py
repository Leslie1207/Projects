print "-----Hello! Welcome to the tip calculator!-----\n"

# input how much the bill was
raw_bill = raw_input("The bill total is: GBP ")
x = float(raw_bill)

# what percentage tip do they want to give
print '-' * 30
tip_percentage = raw_input("What percentage (%) tip would you like to give: ")
# converts number into percentage, divides input by 100
y = float(tip_percentage) / 100

# how many people are in the party?
print '-' * 30
people_present = raw_input("How many people are present: ")
z = int(people_present)

# function takes initial bill
# adds it to worked out percentage (x * y)
# divides by number of people in the party
print '-' * 30
def calculate_bill():
    total_bill = (x + (x * y))/z
    return round(total_bill, 2)

print "Each person owes: GBP",calculate_bill()