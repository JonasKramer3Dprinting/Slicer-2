import math

from gCodeFunctions import *

from globalVariables import *

from printSettings import *

from printSettings2 import *

from optionZero import *

from optionOne import *

from gCodeStart import *

from gCodeEnd import *

printOptions()
if (
    int(
        input(
            "Type in 0 for Standard Settings.\nType in 1 for Costum Settings.\nType in here: "
        )
    )
    == 0
):
    tei, te, tbi, tb, lhi, lh, lwi, lw, fti, ft, fei, fe, rd = (
        210,
        205,
        70,
        65,
        0.24,
        0.12,
        0.5,
        0.4,
        1200,
        1200,
        1200,
        1200,
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
    list, objectHeight = optionZeroOne(lineWidth, placement[0], placement[1])
    print(list)
if option == 1:
    print(list)

# hier wird die zweite Option verwendet, falls diese zuvor angegeben wurde

# hier wird der Code für die erste Schicht angefangen zu schreiben
z = lineHeight
gCodeFirstLayer = m104(extruderTemperature)

# hier werden die gegebenen Punkte abgefahren
gCodeFirstLayer = (
    gCodeFirstLayer + g0(list[0], list[1], z, travelSpeed) + g1retractreversed(8)
)
for a in range(0, len(list) - 2, 2):
    X = list[a]
    Y = list[a + 1]
    x = list[a + 2]
    y = list[a + 3]
    gCodeFirstLayer = gCodeFirstLayer + g1(
        x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeight, pi
    )
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
    list, objectHeight = optionZeroTwo(lineWidth, placement[0], placement[1])
    print(list)
if option == 1:
    print(list)

# hier wird die zweite Option verwendet, falls diese zuvor angegeben wurde

# hier wird der Code für die zweite Schicht angefangen zu schreiben
z = z + lineHeight
gCodeMiddle = m104(extruderTemperature) + m140(bedTemperature)

# hier werden die gegebenen Punkte abgefahren
for a in range(
    0, int(round((objectHeight - lhi) * 10 ** 12)) // int((lineHeight * 10 ** 12))
):

    gCodeMiddle = (
        gCodeMiddle
        + g0(list[0], list[1], z - lineHeight, travelSpeed)
        + g0(list[0], list[1], z, travelSpeed)
        + g1retractreversed(retractionDistance)
    )
    for a in range(0, len(list) - 2, 2):
        X = list[a]
        Y = list[a + 1]
        x = list[a + 2]
        y = list[a + 3]
        gCodeMiddle = gCodeMiddle + g1(
            x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeight, pi
        )
    gCodeMiddle = gCodeMiddle + g1retract(retractionDistance)
    z = z + lineHeight

# mit folgendem Code wird der Startcode festgelegt
gCodeEnd = giveEndCode()

# hier werdden die verschiedenen Codes addiert
gCode = gCodeStart + gCodeFirstLayer + gCodeMiddle + gCodeEnd
print(gCode)

# hier wird der Code abgespeichert
name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(gCode)
