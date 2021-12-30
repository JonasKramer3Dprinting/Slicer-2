import math

from gCodeFunctions import *

from globalVariables import *

from printSettings import *

from printSettings2 import *

from optionZero import *

from optionOne import *

from gCodeStart import *

from gCodeEnd import *

option = printOptions()

if (
    int(
        input(
            "Type in 0 for Standard Settings.\nType in 1 for Costum Settings.\nType in here: "
        )
    )
    == 0
):
    tei, te, tbi, tb, lhi, lh, lwi, lw, fti, ft, fei, fe, rd = (
        205,
        200,
        65,
        60,
        0.24,
        0.12,
        0.5,
        0.4,
        2400,
        4800,
        1200,
        2400,
        8,
    )
else:
    tei, te, tbi, tb, lhi, lh, lwi, lw, fti, ft, fei, fe, rd = printSettings()

extruderTemperature, bedTemperature, lineHeight, retractionDistance = changeOne(
    tei, tbi, lh
)

# mit folgendem Code wird der Startcode festgelegt
gCodeStart = giveStartCode(lh, bedTemperature, extruderTemperature)

(
    extruderTemperature,
    bedTemperature,
    lineHeight,
    lineWidth,
    travelSpeed,
    extrusionSpeed,
    retractionDistance,
) = changeTwo(tei, tbi, lhi, lwi, fti, fei, rd)

placement = placementSettings()

# hier wird die erste Option verwendet, falls dies zuvor angegeben wurde
if option == 0:
    list, listE, objectHeight = optionZeroOne(lineWidth, placement[0], placement[1])
    print(list)
if option == 1:
    optionOneSettings()
    list, listE, objectHeight = optionOne(
        lineWidth,
        placement[0],
        placement[1],
        optionOneSettings1(),
        optionOneSettings2(),
        optionOneSettings3(),
    )
    print(list)

# hier wird die zweite Option verwendet, falls diese zuvor angegeben wurde

# hier wird der Code für die erste Schicht angefangen zu schreiben
z = lineHeight
gCodeFirstLayer = m104(extruderTemperature)

# hier werden die gegebenen Punkte abgefahren



print(len(list), len(list), len(listE), len(listE))



gCodeFirstLayer = (
    gCodeFirstLayer + g0(list[0], list[1], z, travelSpeed) + g1retractreversed(8-8) #es wurden schon 8mm eingezogen und nun müssen wieder 
)
for a in range(0, len(list) - 2, 2):
    x = list[a + 2]
    y = list[a + 3]
    if listE[int(a / 2) + 1] == True:
        X = list[a]
        Y = list[a + 1]
        gCodeFirstLayer = gCodeFirstLayer + g1(
            x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeight, pi
        )
    else:
        gCodeFirstLayer = gCodeFirstLayer + g0(x, y, z, travelSpeed)
gCodeFirstLayer = gCodeFirstLayer + g1retract(retractionDistance)

(
    extruderTemperature,
    bedTemperature,
    lineHeight,
    lineWidth,
    travelSpeed,
    extrusionSpeed,
    retractionDistandance,
) = changeThree(te, tb, lh, lw, ft, fe, rd)

# hier wird die erste Option verwendet, falls diese zuvor angegeben wurde
if option == 0:
    list, listE, objectHeight = optionZeroTwo(lineWidth, placement[0], placement[1])
    print(list)
if option == 1:
    list, listE, objectHeight = optionOne(
        lineWidth,
        placement[0],
        placement[1],
        optionOneSettings1(),
        optionOneSettings2(),
        optionOneSettings3(),
    )
    print(list)

# hier wird die zweite Option verwendet, falls diese zuvor angegeben wurde

# hier wird der Code für die zweite Schicht angefangen zu schreiben
z = round((z + lineHeight), 6)
gCodeMiddle = m104(extruderTemperature) + m140(bedTemperature)

# hier werden die gegebenen Punkte abgefahren
for a in range(
    0, int(round((objectHeight - lhi) * 10 ** 12)) // int((lineHeight * 10 ** 12))
):

    gCodeMiddle = (
        gCodeMiddle
        + g0(list[0], list[1], z - lineHeight, travelSpeed)
        + g0(list[0], list[1], z, travelSpeed) # Bewegung zum Ansatz wird bereits ausgeführt
        + g1retractreversed(retractionDistance)
    )
    for a in range(0, len(list) - 2, 2):
        x = list[a + 2]
        y = list[a + 3]
        if listE[int(a / 2) + 1] == True: # der int ist um eine Einheit höher, siehe im letzten Kommentar
            X = list[a]
            Y = list[a + 1]
            gCodeMiddle = gCodeMiddle + g1(
                x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeight, pi
            )
        else:
            gCodeMiddle = gCodeMiddle + g0(x, y, z, travelSpeed)
    gCodeMiddle = gCodeMiddle + g1retract(retractionDistance)
    z = round((z + lineHeight), 6)

# mit folgendem Code wird der Startcode festgelegt
gCodeEnd = giveEndCode()

# hier werdden die verschiedenen Codes addiert
gCode = gCodeStart + gCodeFirstLayer + gCodeMiddle + gCodeEnd
print(gCode)

# hier wird der Code abgespeichert
name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(gCode)
