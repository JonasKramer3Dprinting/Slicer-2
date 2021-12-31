# mit dieser Funktion wird abgefragt, was genau gedruckt werden soll
def printOptions():
    option = int(
        input(
            "What do you want to print? \nEnter 0 for printing a quader. \nEnter 1 for printing an extruded equilateral polygon. \nEnter your number here: "
        )
    )
    return option


# mit dieser Funktion wird abgefragt, wo das zu druckende Bauteil platziert wird
def placementSettings():
    print("Where should the object be placed?")
    placementX = float(
        input("Give the x-Coordinate, which should be between 50 and 170: ")
    )
    placementY = float(
        input("Give the Y-Coordinate, which should be between 50 and 170: ")
    )
    return [placementX, placementY]
