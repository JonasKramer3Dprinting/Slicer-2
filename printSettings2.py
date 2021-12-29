# mit dieser Funktion wird abgefragt, was genau gedruckt werden soll
def printOptions():
    global option
    option = int(
        input(
            "What do you want to print? \nEnter 0 for printing a quader.\nEnter 1 for printing an extruded equilateral polygon.  \nEnter 2 for printing a zylinder. \nEnter 3 for printing an extruded surface made of connected corners. \nEnter your number here: "
        )
    )


# mit dieser Funktion wird abgefragt, wo das zu druckende Bauteil platziert wird
def placementSettings():
    print("Where should the object be placed?")
    placementX = float(
        input("Give the x-Coordinate, which should be between 60 and 180: ")
    )
    placementY = float(
        input("Give the Y-Coordinate, which should be between 60 and 180: ")
    )
    return [placementX, placementY]
