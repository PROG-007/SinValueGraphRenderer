import os
import math
import time
os.system("cls")
switch = False
degreeSpanSingleScreen = 180
verticalPrecisionParameter = 50
graphYPosIndex = 0
degreeFreeFlow = 0
steepness = 10
character = ['O', '#']
characterSelection = False

while True:
    os.system("cls")
    a = str(input(
        f"Enter the amount of degrees you want to span in 1 screen ({degreeSpanSingleScreen} is default and recommended) : "))
    if a.isdigit():
        if int(a) > 0:
            degreeSpanSingleScreen = int(a)
            break
        else:
            print(f"Please enter a positive value not anything else!")
            os.system("PAUSE")
    else:
        print("Please enter a numeric value not anything else!")
        os.system("PAUSE")
while True:
    os.system("cls")
    a = str(input(
        f"Enter the amount of Vertical Precision you want in the curve ({verticalPrecisionParameter} is default and recommended) : "))
    if a.isdigit():
        if int(a) > 0:
            verticalPrecisionParameter = int(a)
            break
        else:
            print("Please enter a positive value not anything else!")
            os.system("PAUSE")
    else:
        print("Please enter a numeric value not anything else!")
        os.system("PAUSE")
while True:
    os.system("cls")
    a = str(input(
        f"Enter the amount of steepness you want ({steepness} is default and recommended) : "))
    if a.isdigit():
        if int(a) > 0:
            steepness = int(a)
            break
        else:
            print("Please enter a positive value not anything else!")
            os.system("PAUSE")
    else:
        print("Please enter a numeric value not anything else!")
        os.system("PAUSE")
while True:
    os.system("cls")
    b = str(input("Which do you prefer: \n[A] Live updating(moving) wave or all points in wave\n are updated simultaneously\n[B] Point by point update of each point in the wave and a \nlive refresh as the new wave overlaps the old. : "))
    if b.lower() == 'a':
        switch = True
        break
    elif b.lower() == 'b':
        switch = False
        break
    else:
        print("Please enter A or B as an option not anything else!")
        os.system("PAUSE")

a = [[' ']*degreeSpanSingleScreen for i in range(verticalPrecisionParameter+1)]


def printGraph():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print("")


while True:
    for i in range(degreeSpanSingleScreen):
        sinVal = int(math.sin(math.radians(degreeFreeFlow))*10)
        if sinVal > 10:
            sinVal = 10
        for j in range(verticalPrecisionParameter+1):
            a[j][graphYPosIndex] = " "
        a[(verticalPrecisionParameter//2)-(sinVal)
          ][graphYPosIndex] = character[characterSelection]
        degreeFreeFlow += steepness
        graphYPosIndex += 1
        if graphYPosIndex >= degreeSpanSingleScreen-1:
            graphYPosIndex = 0
            if not switch:
                characterSelection = not characterSelection
        if not switch:
            break
    printGraph()
    time.sleep(0.1)
    os.system("cls")
