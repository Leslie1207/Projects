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
maxRating = 2.375
minRating = 0

def qbRating (att, comp, yds,td, inter):
    a = (((comp/att)-0.3) * 5)
    b = (((yds/att)-3) * 0.25)
    c = ((td/att) * 20)
    d = (2.375 - ((inter/att) * 25))   
    if a > maxRating:
        a = maxRating
    if a < minRating:
        a = minRating
    if b > maxRating:
        b = maxRating
    if b < minRating:
        b = minRating
    if c > maxRating:
        c = maxRating
    if c < minRating:
        c = minRating
    if d > maxRating:
        d = maxRating
    if d < minRating:
        d = minRating       
    passerRating = ((a + b + c + d)/6) * 100
    return round(passerRating, 1)
    

print(("\n%s's QB rating is: ") %(qbName), qbRating(att, comp, yds, td, inter)) 

