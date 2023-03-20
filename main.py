import os
import math

degrees = 181
degreesIndex=0
degreesVar = 0
a = [[' ']*degrees for i in range(21)]


def printGraph():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print()


while True:
    os.system("cls")
    sinVal = int(math.sin(degreesIndex/10)*10)
    if sinVal > 9:
        sinVal = 9
    for i in range(21):
        a[i][degreesVar] = " "
    a[10-(sinVal)][degreesVar] = "*"
    printGraph()
    if degreesVar >= degrees-1:
        degreesVar = 0
    degreesVar += 1
    degreesIndex += 1
