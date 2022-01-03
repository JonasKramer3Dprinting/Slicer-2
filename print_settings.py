# hier wird die Funktion definiert, mit der die Druckeinstellungen gesetzt werden
def print_settings():
    tei = float(input("Initial Layer Extruder Temperature: "))
    te = float(input("Extruder Temperature: "))
    tbi = float(input("Initial Layer Bed Temperature: "))
    tb = float(input("Bed Temperature: "))
    lhi = float(input("Initial Layer Heigth: "))
    lh = float(input("Layer Heigth: "))
    lwi = float(input("Initial Layer Line Width: "))
    lw = float(input("Line Width: "))
    fti = float(input("Initial Layer Travel Speed: "))
    ft = float(input("Travel Speed: "))
    fei = float(input("Initial Layer Extrusion Speed: "))
    fe = float(input("Extrusion Speed: "))
    rd = float(input("Retract Distance: "))
    return tei,te,tbi,tb,lhi,lh,lwi,lw,fti,ft,fei,fe,rd


# hier werden die Druckeinstellungen auf die Werte der ersten Extrusionslinien gesetzt
def change_one(tei,tbi,lh):
    return tei,tbi,lh,10


# hier werden die Druckeinstellungen auf die Werte der ersten Ebene gesetzt
def change_two(tei,tbi,lhi,lwi,fti,fei,rd):
    return tei,tbi,lhi,lwi,fti,fei,rd


# hier werden die Druckeinstellungen auf die Werte der zweiten bis zur letzten Ebene gesetzt
def change_three(te,tb,lh,lw,ft,fe,rd):
    return te,tb,lh,lw,ft,fe,rd


# mit dieser Funktion wird abgefragt, was genau gedruckt werden soll
def print_options():
    option = int(
        input(
            "What do you want to print? \nEnter 0 for printing a quader. \nEnter 1 for printing an extruded equilateral polygon. \nEnter your number here: "
        )
    )
    return option


# mit dieser Funktion wird abgefragt, wo das zu druckende Bauteil platziert wird
def placement_settings():
    print("Where should the object be placed?")
    placement_x = float(
        input("Give the x-Coordinate, which should be between 50 and 170: ")
    )
    placement_y = float(
        input("Give the Y-Coordinate, which should be between 50 and 170: ")
    )
    return [placement_x, placement_y]