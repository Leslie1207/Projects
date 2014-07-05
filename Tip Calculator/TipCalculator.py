print "-----Hello! Welcome to the tip calculator!-----\n"

raw_bill = raw_input("The bill total is: GBP ")
x = float(raw_bill)

print '-' * 30
tip_percentage = raw_input("What percentage (%) tip would you like to give: ")
y = float(tip_percentage) / 100

print '-' * 30
people_present = raw_input("How many people are present: ")
z = int(people_present)

print '-' * 30
def calculate_bill():
    total_bill = (x + (x * y))/z
    return round(total_bill, 2)

print "Each person owes: GBP", calculate_bill()