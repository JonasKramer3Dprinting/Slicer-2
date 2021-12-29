from globalVariables import *

corners = 0
radius = 0.0
deviation = 0.0


def optionOneSettings():
    global radius
    global corners
    corners = int(input("How many corners should the quilateral polygon have: "))
    if (
        int(
            input("Input 0 for giving the radius, input 1 for giving the sidelenghth: ")
        )
        == 0
    ):
        radius = float(input("Radius: "))
    else:
        sidelength = float(input("sidelength: "))
        radius = sidelength / math.sin(math.pi / corners) / 2


def optionOneSettings1():
    return radius


def optionOneSettings2():
    return corners


lineWidth = 0.5


def optionOne(lineWidth, placementX, placementY, radius, corners, height):
    global list
    global deviation
    a = 180 - 360 / corners
    deviation = (lineWidth ** 2 + (lineWidth / math.tan(math.pi/180 * a) + lineWidth / math.sin(math.pi/180 * a)) ** 2) ** 0.5
    print(deviation)
    radius = radius - deviation/2 #Abweichung der äußersten Linie wird korrigiert
    list = []
    while True:
        if radius < 0:
            break #Schleife wir gebrochen, sobald die Düse sich zum Mittelpunkt des Polygons vorgearbeitet hat
        for a in range(0, corners + 1, 1):
            angle = a * 360 / corners
            list.append(math.cos(math.pi / 180 * angle) * radius)
            list.append(math.sin(math.pi / 180 * angle) * radius)
        radius = radius - deviation #Abweichungen werden korrigiert
    for a in range(0, len(list), 2):
        list[a] = list[a] + placementX
        list[a + 1] = list[a + 1] + placementY
    print(list)
    return list, height


optionOneSettings()
optionOne(lineWidth, 100, 100, optionOneSettings1(), optionOneSettings2(), 5)
