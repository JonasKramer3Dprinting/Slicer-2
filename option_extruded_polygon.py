from global_variables import *

corners = 0
radius = 0.0
deviation = 0.0
height = 0.0


def option_extruded_polygon_settings():
    global radius
    global corners
    global height
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
        radius = sidelength / math.sin(math.pi / corners) / 2 #der Radius wird anhand der Seitenlänge und der Anzahl der Ecken berechnet
    height = float(input("Height of the object: "))


def option_one_settings1():
    return radius


def option_one_settings2():
    return corners


def option_one_settings3():
    return height


def option_one(line_width, placement_x, placement_y, radius, corners, height):
    global list
    global list_e
    list_e = []
    list = []
    global deviation
    a = 180 - 360 / corners
    deviation = (
        line_width ** 2
        + (
            line_width / math.tan(math.pi / 180 * a)
            + line_width / math.sin(math.pi / 180 * a)
        )
        ** 2
    ) ** 0.5  # hier wird die Abweichung berechnet
    print(deviation)
    radius = radius - deviation / 2  # Abweichung der äußersten Linie wird korrigiert
    while True:
        if radius < (line_width / 2):
            break  # Schleife wir gebrochen, sobald die Düse sich zum Mittelpunkt des Polygons vorgearbeitet hat
        angle = 0  # in dieser und den nächsten 3 Zeilen wird der erste Punkt gegeben und dafür der boolianische Wert False eingetragen, da der Extruder zum Ansatzpunkt einer Ebene sich nur bewegen soll und bei dieser Bewegung kein Material extrudiert werden soll
        list.append(
            math.cos(math.pi / 180 * angle) * radius
        )  # der in der letzten Zeile angesprochene Ansatz kommt vor, jedes mal, wenn bevor ein kleiners Polygon gedruckt wird, der Extruder sich um die Länge der Abweichung nach innen bewegen soll
        list.append(math.sin(math.pi / 180 * angle) * radius)
        list_e.append(
            False
        )  # zum ersten Punkt der Liste wird sich bewegt, ohne Material zu extrudieren
        for a in range(1, corners + 1, 1):
            angle = a * 360 / corners
            list.append(math.cos(math.pi / 180 * angle) * radius)  # xKoordinate
            list.append(math.sin(math.pi / 180 * angle) * radius)  # yKoordinate
            list_e.append(
                True
            )  # True, da Material extrudiert werden soll, bei der ansteuerung alle gegebenen Punkte, um die Seitenlinien des Polygons drucken zu können
        radius = (
            radius - deviation
        )  # die Düse des Druckers bewegt sich um die Distanz der Abweichung nach innen, da beim erneuten Ablaufen der Schleife ein kleineres Polygon gedruckt wird
    for a in range(0, len(list), 2):
        list[a] = round(
            (list[a] + placement_x), 6
        )  # die x und y Koordinaten werden in diesen zwei Zeilen gerundet, da die Motoren des Druckers die Koordinaten nicht genauer ansteuern kann
        list[a + 1] = round((list[a + 1] + placement_y), 6)
    print(list)
    return (
        list, list_e, 
        height,
    )  # die Liste der Punkte und die Objekthöhe werden bei dieser Funktion am Ende wiedergegeben