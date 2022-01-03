from global_variables import *

corners = 0  # Anzahl der Ecken des Polygons
radius = 0.0  # "Radius" des Polygons
deviation = 0.0  # Abweichungsdistanz
height = 0.0  # Objekthöhe

# mit dieser Funktion werden die Maßen des Objektes angegeben
def option_extruded_polygon_settings():
    global radius
    global corners
    global height
    corners = int(input("How many corners should the quilateral polygon have: "))
    # hier kann der Radius angegeben werden
    if (
        int(
            input("Input 0 for giving the radius, input 1 for giving the sidelenghth: ")
        )
        == 0
    ):
        radius = float(input("Radius: "))
    # hier kann die Seitenlänge angegeben werden
    else:
        sidelength = float(input("sidelength: "))
        radius = (
            sidelength / math.sin(math.pi / corners) / 2
        )  # der Radius wird anhand der Seitenlänge und der Anzahl der Ecken berechnet
    height = float(input("Height of the object: "))


# diese Funktion gibt den Radius zurück
def option_one_settings1():
    return radius


# diese Funktion gibt die Anzahl der Ecken zurück
def option_one_settings2():
    return corners


# diese Funktion gibt die Höhe des Objektes zurück
def option_one_settings3():
    return height


# diese Funktion gibt die Liste, die Extrusionsliste und die Objekthöhe wieder
def option_one(line_width, placement_x, placement_y, radius, corners, height):
    global list
    global list_e
    list_e = []
    list = []
    global deviation
    a = 180 - 360 / corners
    # hier wird die Abweichung berechnet
    deviation = (
        line_width ** 2
        + (
            line_width / math.tan(math.pi / 180 * a)
            + line_width / math.sin(math.pi / 180 * a)
        )
        ** 2
    ) ** 0.5
    print(deviation)
    # Abweichung der äußersten Linie wird korrigiert
    radius = radius - deviation / 2
    while True:
        if radius < (line_width / 2):
            # Schleife wir gebrochen, sobald die Düse sich zum Mittelpunkt des Polygons vorgearbeitet hat
            break
        angle = 0
        # der erste Punkt wird zur Liste hinzugefügt
        list.append(math.cos(math.pi / 180 * angle) * radius)  # x Koordinate
        list.append(math.sin(math.pi / 180 * angle) * radius)  # y Koordinate
        # der Extrusionswert des ersten Punktes wird zur Liste hinzugefügt, hier ist der Wert False, der die Düse sich zu diesem Punkt bewegen soll, ohne Material zu extrudieren
        list_e.append(False)
        # die Punkte eines Polygons werden ermittelt
        for a in range(1, corners + 1, 1):
            angle = a * 360 / corners
            list.append(math.cos(math.pi / 180 * angle) * radius)  # x Koordinate
            list.append(math.sin(math.pi / 180 * angle) * radius)  # y Koordinate
            # True, da Material extrudiert werden soll, bei der ansteuerung alle gegebenen Punkte, um die Seitenlinien des Polygons drucken zu können
            list_e.append(True)
        # die Düse des Druckers bewegt sich um die Distanz der Abweichung nach innen, da beim erneuten Ablaufen der Schleife ein kleineres Polygon gedruckt wird
        radius = radius - deviation
    # alle Koodinaten werden hier gerundet
    for a in range(0, len(list), 2):
        # die x und y Koordinaten werden in diesen zwei Zeilen gerundet, da die Motoren des Druckers die Koordinaten nicht genauer ansteuern kann
        list[a] = round((list[a] + placement_x), 6)
        list[a + 1] = round((list[a + 1] + placement_y), 6)
    print(list)
    # die Liste der Punkte und die Objekthöhe werden bei dieser Funktion am Ende wiedergegeben
    return (
        list,
        list_e,
        height,
    )
