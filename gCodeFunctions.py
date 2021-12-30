e = 0.0

# hier ist die Funktion zur Extrusionsberechnung für lineare Bewegungen
def find_factor(x, y, X, Y, lineWidth, lineHeigth, pi):
    lineDistance = ((X - x) ** 2 + (Y - y) ** 2) ** 0.5
    global e
    e = e + (lineDistance * lineWidth * lineHeigth * 4) / (1.75 ** 2 * pi)
    e = round(e,6)
    return e


# nun werden alle Funktionen geschrieben, die als Rückgabe den benötigten gCode ausgeben
def g0(x, y, z, travelSpeed):
    s = "G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " F" + str(travelSpeed) + "\n"
    return s


def g1(x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeigth, pi):
    s = (
        "G1 X"
        + str(x)
        + " Y"
        + str(y)
        + " Z"
        + str(z)
        + " E"
        + str(find_factor(x, y, X, Y, lineWidth, lineHeigth, pi))
        + " F"
        + str(extrusionSpeed)
        + "\n"
    )
    return s


def g1retract(retractionDistance):
    global e
    e = e - retractionDistance
    s = "G1 E" + str(e) + "\n"
    return s


def g1retractreversed(retractionDistance):
    global e 
    e = e + retractionDistance
    s = "G1 E" + str(e) + "\n"
    return s


def g17():
    s = "G17; change to xy \n"
    return s


def g18():
    s = "G18; change to xz \n"
    return s


def g19():
    s = "G19; change to yz \n"
    return s


def g20():
    s = "G20; change to imperial system \n"
    return s


def g21():
    s = "G21; change to metric system \n"
    return s


def g28():
    s = "G28; homing \n"
    return s


def g90():
    s = "G90; change to absolutive positioning \n"
    return s


def g91():
    s = "G91; change to relative positioning \n"
    return s


def g92(x, y, z):
    x = 0
    y = 0
    z = 0
    s = "G92 X" + str(x) + " Y" + str(y) + " Z" + str(z) + "\n"
    return s


def m82():
    s = "M82; extruder changes to absolutive positioning \n"
    return s


def m83():
    s = "M83; extruder changes to relative positioning \n"
    return s


def m104(extruderTemperature):
    s = "M104 S" + str(extruderTemperature) + "\n"
    return s


def m109(extruderTemperature):
    s = "M109 S" + str(extruderTemperature) + "\n"
    return s


def m140(bedTemperature):
    s = "M140 S" + str(bedTemperature) + "\n"
    return s


def m190(bedTemperature):
    s = "M190 S" + str(bedTemperature) + "\n"
    return s
