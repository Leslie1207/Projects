#Pythagoras' Theorem

import math

while True:

    chooseSide = input("Which side do you want to find? A, B or C? ")
    
    if chooseSide in ["C", "c"]:
        unitsOfMeasure = input("What units of measure are you using? ")
        def findSideC (sideA, sideB):
            cSquare = (sideA ** 2) + (sideB ** 2)
            sideC = math.sqrt(cSquare)
            return sideC
        
        sideA = float(input("Side A: "))
        sideB = float(input("Side B: "))
        
        test1 = findSideC(sideA, sideB)
        print("Side C is ", test1, unitsOfMeasure)
        
    elif chooseSide in ["A", "a"]:
        unitsOfMeasure = input("What units of measure are you using? ")
        def findSideA (sideC, sideB):
            aSquare = (sideC ** 2) - (sideB ** 2)
            sideA = math.sqrt(aSquare)
            return sideA
        
        sideC = float(input("Side C: "))
        sideB = float(input("Side B: "))

        test2 = findSideA(sideC, sideB)
        print("Side A is ", test2, unitsOfMeasure)

    elif chooseSide in ["B", "b"]:
        unitsOfMeasure = input("What units of measure are you using? ")
        def findSideB (sideC, sideA):
            bSquare = (sideC ** 2) - (sideA ** 2)
            sideB = math.sqrt(bSquare)
            return sideB
            
        sideC = float(input("Side C: "))
        sideA = float(input("Side A: "))

        test3 = findSideB(sideC, sideA)
        print("Side B is ", test3, unitsOfMeasure)

    elif chooseSide not in ["A", "a", "B", "b", "C", "c"]:
        print("I do not understand, choose A, B or C.")
