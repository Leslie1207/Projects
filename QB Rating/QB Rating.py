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

def clamp(x, min_n, max_n):
    return min(max(x, min_n), max_n)

def qbRating (att, comp, yds,td, inter):
    a = (((comp/att)-0.3) * 5)
    b = (((yds/att)-3) * 0.25)
    c = ((td/att) * 20)
    d = (2.375 - ((inter/att) * 25))   

    a = clamp(a, min_n=0, max_n=2.375)
    b = clamp(b, min_n=0, max_n=2.375) 
    c = clamp(c, min_n=0, max_n=2.375)
    d = clamp(d, min_n=0, max_n=2.375)

    return(a)
    return round(((a + b + c + d)/6) * 100, 1)

print(("\n%s's QB rating is: ") %(qbName), qbRating(att, comp, yds, td, inter)) 

