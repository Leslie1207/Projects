#QB Passer Rating Calculator

"""
ATT = Number of passing attempts
COMP = Number of completions
YDS = Passing yards
TD = Touchdown passes
INT = Interceptions
"""

qbName = str(input("What is the name of the QB? "))
att = float(input("Please input the number of PASSING ATTEMPTS: "))
comp = float(input("Please input the number of PASSING COMPLETIONS: "))
yds = float(input("Please input the number of PASSING YARDS: "))
td = float(input("Please input the number of TOUCHDOWN PASSES: "))
inter = float(input("Please input the number of INTERCEPTIONS: "))

def qbRating (att, comp, yds,td, inter):
    a = (((comp/att)-0.3) * 5)
    b = (((yds/att)-3) * 0.25)
    c = ((td/att) * 20)
    d = (2.375 - ((inter/att) * 25))   
    if a > 2.375:
        a = 2.375
    if a < 0:
        a = 0
    if b > 2.375:
        b = 2.375
    if b < 0:
        b = 0
    if c > 2.375:
        c = 2.375
    if c < 0:
        c = 0
    if d > 2.375:
        d = 2.375
    if d < 0:
        d = 0       
    passerRating = ((a + b + c + d)/6) * 100
    return round(passerRating, 1)
    

print(("\n%s's QB rating is: ") %(qbName))
print(qbRating(att, comp, yds, td, inter)) 
