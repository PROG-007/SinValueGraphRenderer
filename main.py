import os
import math

degreeSpanSingleScreen = 90
verticalPrecisionParameter = 50
graphYPosIndex = 0
degreeFreeFlow = 0
steepness = 10

a = [[' ']*degreeSpanSingleScreen for i in range(verticalPrecisionParameter+1)]

def printGraph():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print()
while True:
    sinVal = int(math.sin(math.radians(degreeFreeFlow))*10)
    if sinVal > 10:
        sinVal = 10
    for i in range(verticalPrecisionParameter+1):
        a[i][graphYPosIndex] = " "
    a[(verticalPrecisionParameter//2)-(sinVal)][graphYPosIndex] = "."
    printGraph()
    if graphYPosIndex >= degreeSpanSingleScreen-1:
        graphYPosIndex = 0
    degreeFreeFlow += steepness
    graphYPosIndex += 1
    os.system("cls")
