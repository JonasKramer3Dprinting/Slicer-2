from globalVariables import *
def optionOneSettings1():
    return int(input("How many corners should the quilateral polygon have: "))

def optionTwoSettings2():
    if int(input("Input 0 for giving the radius, input 1 for giving the sidelenghth: ")) = 0:
        print("Hello")

def radiusBerechnen(anzahlEcken, seitenlänge):
    return seitenlänge/math.sin(math.pi/anzahlEcken)/2

#eingabe der Daten
r = float(input("Radius: "))
c = int(input("Corners: "))
degree = 0

#Punkteauswertung
for a in range(0, c, 1):
    degree = a * 360 / c
    print(degree)
    list.append(math.cos(math.pi / 180 * degree) * r)
    list.append(math.sin(math.pi / 180 * degree) * r)

#erster und zweiter Punkt werden erneut hinten drangehängt, da die Düse als letztes innerhalb einer Bahn zum Uhrsprungspunkt zurückkehren soll
list.append(list[0])
list.append(list[1])

#Koordinaten, welche nahe Null liegen werden auf null gesetzt
for a in range(0, len(list), 1):
    if list[a] < 0.000000000001:
        if list[a] > -0.0000000001:
            list[a] = 0
    list[a] = list[a] + 50

print(list)


#def optionZeroOne(lineWidth, placementX, placementY):
   # return optionZero(lineWidth,placementX, placementY, optionZeroSettings1(), optionZeroSettings2(), optionZeroSettings3())
##
#def optionZeroTwo(lineWidth, placementX, placementY):
    return optionZero(lineWidth, placementX, placementY, length, width, height)

#def optionZero(lineWidth,placementX,placementY, length, width, height):