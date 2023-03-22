import os
import math
import time


switch = False # user defined

degreeSpanSingleScreen = 180 # user defined
degreeSpanSingleScreenFeasibleLimit = 180 # constant
steepness = 10 # user defined
steepnessBreakingPoint = 30 # constant

graphPadding = 50 # constant
graphYPosIndex = 0 # dynamic
degreeFreeFlow = 0 # dynamic

character = ['O', '#'] # constant
characterSelection = True # dynamic

def printGraph():
    for i in range(len(graphData)):
        for j in range(len(graphData[i])):
            print(graphData[i][j], end="")
        print("")

def customInputHandler(varA, varB, correctionConstant = 1):
    while True:
        os.system("cls")
        a = str(input(f"Enter the amount of steepness you want [1 < value < {varB}(Breaking Point)] [{varA} is default and recommended for best results] : "))
        if a.isdigit():
            if int(a) > 1:
                temp = int(a)//correctionConstant
                varA = ((temp)-((temp)%2))*correctionConstant
                break
            else:
                print(f"Please enter a numeric value in the range [1 < value < {varB}(Breaking Point)] not anything else!")
                os.system("PAUSE")
        else:
            print("Please enter a numeric value not anything else!")
            os.system("PAUSE")
    return varA

os.system("cls")
degreeSpanSingleScreen = customInputHandler(degreeSpanSingleScreen, degreeSpanSingleScreenFeasibleLimit, 10)
steepness = customInputHandler(steepness, steepnessBreakingPoint)

while True: # render type switch selection input handler
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

graphData = [[' ']*degreeSpanSingleScreen for i in range(graphPadding+1)] # empty graph declaration

while True:
    for i in range(degreeSpanSingleScreen):
        sinVal = int(math.sin(math.radians(degreeFreeFlow))*10)
        if sinVal > 10:
            sinVal = 10 # capping the sin value for additional smooothness
        for j in range(graphPadding+1):
            graphData[j][graphYPosIndex] = " "
        graphData[(graphPadding//2)-(sinVal)
          ][graphYPosIndex] = character[characterSelection]# interpretting sin value for degree into a 2d array
        degreeFreeFlow += steepness
        graphYPosIndex += 1
        if graphYPosIndex >= degreeSpanSingleScreen-1:
            graphYPosIndex = 0 # out of range error prevention
            if not switch:
                characterSelection = not characterSelection
        if not switch:
            break
    printGraph() # printing the updated graph
    os.system("cls")
