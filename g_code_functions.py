e = 0.0

# hier ist die Funktion zur Extrusionsberechnung für lineare Bewegungen
def find_factor(x, y, X, Y, line_width, line_height, pi):
    line_distance = ((X - x) ** 2 + (Y - y) ** 2) ** 0.5
    global e
    e = e + (line_distance * line_width * line_height * 4) / (1.75 ** 2 * pi)
    e = round(e,6)
    return e


# nun werden alle Funktionen geschrieben, die als Rückgabe den benötigten gCode ausgeben

# dieser Befehl erzeugt eine lineare Bewegung ohne Extrusion
def g0(x, y, z, travel_speed):
    s = "G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " F" + str(travel_speed) + "\n"
    return s

# dieser Befehl erzeugt eine lineare Bewegung mit Extrusion
def g1(x, y, z, extrusion_speed, X, Y, line_width, line_height, pi):
    s = (
        "G1 X"
        + str(x)
        + " Y"
        + str(y)
        + " Z"
        + str(z)
        + " E"
        + str(find_factor(x, y, X, Y, line_width, line_height, pi))
        + " F"
        + str(extrusion_speed)
        + "\n"
    )
    return s

# dieser Befehl führt einen Filamenteinzug aus
def g1_retract(retraction_distance):
    global e
    e = e - retraction_distance
    s = "G1 E" + str(e) + "\n"
    return s

# dieser Befehl führt den Gegensatz vom Filamenteinzug aus, da Filament das eingezogen wurde, auch wieder zum Düsenanfang gedrückt werden muss
def g1_retractreversed(retraction_distance):
    global e 
    e = e + retraction_distance
    s = "G1 E" + str(e) + "\n"
    return s

# mit diesem Befehl wechselt der Drucker zur xy-Ebene, dies ist hauptsächlich für Kreisbewegungen wichtig
def g17():
    s = "G17; change to xy \n"
    return s

# mit diesem Befehl wechselt der Drucker zur xz-Ebene, dies ist hauptsächlich für Kreisbewegungen wichtig
def g18():
    s = "G18; change to xz \n"
    return s

# mit diesem Befehl wechselt der Drucker zur yz-Ebene, dies ist hauptsächlich für Kreisbewegungen wichtig
def g19():
    s = "G19; change to yz \n"
    return s

# mit diesem Befehl wechselt der Drucker auf das imperiale System (Distanzen sind nun in Zoll)
def g20():
    s = "G20; change to imperial system \n"
    return s

# mit diesem Befehl wechelt der Drucker auf das metrische System (Distanzen sind nun in mm)
def g21():
    s = "G21; change to metric system \n"
    return s

# mit diesem Befehl steuern die Achsen des Druckers die Nullstellen an
def g28():
    s = "G28; homing \n"
    return s

# mit diesem Befehl wecheln die Achsen des Druckers auf absolute Positionierung
def g90():
    s = "G90; change to absolutive positioning \n"
    return s

# mit diesem Befehl wecheln die Achsen des Druckers auf relative Positionierung
def g91():
    s = "G91; change to relative positioning \n"
    return s

# der Drucker setzt die aktuellen Koordinaten auf die hier neu gegebenen 
def g92(x, y, z):
    x = 0
    y = 0
    z = 0
    s = "G92 X" + str(x) + " Y" + str(y) + " Z" + str(z) + "\n"
    return s

# der Extruder Motor des Druckers wechselt auf absolute Positionierung
def m82():
    s = "M82; extruder changes to absolutive positioning \n"
    return s

# der Extruder Motor der Druckers wechelt auf relative Positionierung
def m83():
    s = "M83; extruder changes to relative positioning \n"
    return s

# der Extruder heizt auf die gegebene Temperatur vor, das Programm läuft weiter
def m104(extruder_temperature):
    s = "M104 S" + str(extruder_temperature) + "\n"
    return s

# der Extruder heizt auf die gegebene Temperatur vor, das Programm wartet, bis die gegebene Temperatur erreicht ist
def m109(extruder_temperature):
    s = "M109 S" + str(extruder_temperature) + "\n"
    return s

# das Bett heizt auf die gegebene Temperatur vor, das Programm läuft weiter
def m140(bed_temperature):
    s = "M140 S" + str(bed_temperature) + "\n"
    return s

# das Bett heizt auf die gegebene Temperatur vor, das Programm wartet, bis die gegebene Temperatur erreicht ist
def m190(bed_temperature):
    s = "M190 S" + str(bed_temperature) + "\n"
    return s
