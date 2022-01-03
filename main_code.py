from global_variables import *

from g_code_functions import *

from print_settings import *

from option_quader import *

from option_extruded_polygon import *

from g_code_start import *

from g_code_end import *

# die Option, die gedruckt werden soll wird abgefragt
option = print_options()

# es wird abgefragt, ob die Standard Druckeinstellungen verwendet werden sollen, oder eigene (die eigenen können folgend eingegeben werden, falls dies vorher angegeben wurde)
if (
    int(
        input(
            "Type in 0 for Standard Settings.\nType in 1 for Costum Settings.\nType in here: "
        )
    )
    == 0
):
    tei, te, tbi, tb, lhi, lh, lwi, lw, fti, ft, fei, fe, rd = (
        205,
        200,
        65,
        60,
        0.12,
        0.12,
        0.4,
        0.4,
        2400,
        4800,
        1200,
        2400,
        8,
    )
else:
    tei, te, tbi, tb, lhi, lh, lwi, lw, fti, ft, fei, fe, rd = print_settings()

# die Druckeinstellungen werden an die ersten beiden Startlinien angepasst
extruder_temperature, bed_temperature, line_height, retraction_distance = change_one(
    tei, tbi, lh
)

# mit folgendem Code wird der Startcode festgelegt
g_code_start = give_start_code(lh, bed_temperature, extruder_temperature)

(
    extruder_temperature,
    bed_temperature,
    line_height,
    line_width,
    travel_speed,
    extrusion_speed,
    retraction_distance,
) = change_two(tei, tbi, lhi, lwi, fti, fei, rd)

# die Positionierung des zu druckenden Objektes wird festgelegt
placement = placement_settings()

# hier werden Liste, Extrusionsliste und Objekthöhe ermittelt in Abhängigkeit davon, welche Druckoption gewählt wurde (alles nur für die erste Schicht)
if option == 0:
    list, list_e, object_height = option_quader_one(
        line_width, placement[0], placement[1]
    )
    print(list)
if option == 1:
    option_extruded_polygon_settings()
    list, list_e, object_height = option_one(
        line_width,
        placement[0],
        placement[1],
        option_one_settings1(),
        option_one_settings2(),
        option_one_settings3(),
    )
    print(list)

# die z Koordinate wird auf den Wert der Schichthöhe gesetzt, welcher aktuell dem Wert der Höhe der ersten Schicht entspricht
z = line_height

print(len(list), len(list), len(list_e), len(list_e))

# es wurden schon 8mm eingezogen und nun müssen wieder 8mm vorgeschoben werden
g_code_first_layer = g0(list[0], list[1], z, travel_speed) + g1_retractreversed(8 - 8)

# die Liste an Punkten der ersten Schicht wird abgefahren
for a in range(0, len(list) - 2, 2):
    x = list[a + 2]
    y = list[a + 3]
    # für Bewegungen mit Extrusion
    if list_e[int(a / 2) + 1] == True:
        X = list[a]
        Y = list[a + 1]
        g_code_first_layer = g_code_first_layer + g1(
            x, y, z, extrusion_speed, X, Y, line_width, line_height, pi
        )
    # für Bewegungen ohne Extrusion
    else:
        g_code_first_layer = g_code_first_layer + g0(x, y, z, travel_speed)

# nach der Beendung der ersten Schicht wird Material eingezogen
g_code_first_layer = g_code_first_layer + g1_retract(retraction_distance)

# die Druckeinstellungen werden an die zweite Schicht angepasst
(
    extruder_temperature,
    bed_temperature,
    line_height,
    line_width,
    travel_speed,
    extrusion_speed,
    retractionDistandance,
) = change_three(te, tb, lh, lw, ft, fe, rd)

# hier werden Liste, Extrusionsliste und Objekthöhe ermittelt in Abhängigkeit davon, welche Druckoption gewählt wurde (alles für die Schichten nach der ersten Schicht)
if option == 0:
    list, list_e, object_height = option_quader_two(
        line_width, placement[0], placement[1]
    )
    print(list)
if option == 1:
    list, list_e, object_height = option_one(
        line_width,
        placement[0],
        placement[1],
        option_one_settings1(),
        option_one_settings2(),
        option_one_settings3(),
    )
    print(list)
    
# die Höhe wird auf den Wert der Höhe der ersten Schicht + der Höhe der zweiten Schicht gesetzt
z = round((z + line_height), 6)

# die neuen Temperaturen werden dem Drucker übermittelt, der Druck läuft aber weiter, siehe g_code_functions
g_code_middle = m104(extruder_temperature) + m140(bed_temperature)

# die Liste an Punkten, für die zweite bis zur letzten Schicht, werden abgefahren und nach jeder Schicht die Höhe gewechselt
for a in range(
    0, int(round((object_height - lhi) * 10 ** 12)) // int((line_height * 10 ** 12))
):

    g_code_middle = (
        g_code_middle
        + g0(list[0], list[1], z - line_height, travel_speed)
        # auf folgende drei Zeilen wird weiter unten verwiesen
        + g0(list[0], list[1], z, travel_speed)
        # Material wird vorgeschoben da es zuvor eingezogen wurde
        + g1_retractreversed(retraction_distance)
    )
    for a in range(0, len(list) - 2, 2):
        x = list[a + 2]
        y = list[a + 3]
        # für Bewegungen mit Extrusion
        if (
            # der Wert ist int(a/2) + 1 und nicht int(a/2) da der erste Punkt schon zuvor angesteuert wurde, siehe zwei Kommentare weiter oben
            list_e[int(a / 2) + 1]
            == True
        ):
            X = list[a]
            Y = list[a + 1]
            g_code_middle = g_code_middle + g1(
                x, y, z, extrusion_speed, X, Y, line_width, line_height, pi
            )
        # für Bewegungen ohne Extrusion
        else:
            g_code_middle = g_code_middle + g0(x, y, z, travel_speed)
    # Material wird eingezogen (und auch später wieder vorgeschoben, siehe vier Kommentare weiter oben)
    g_code_middle = g_code_middle + g1_retract(retraction_distance)
    # die Höhe wird nach jeder beendeten Schicht um jeweils eine Schichthöhe vergrößert
    z = round((z + line_height), 6)

# mit folgendem Code wird der Endcode festgelegt
g_code_end = give_end_code()

# hier werdden die verschiedenen codes addiert
g_code = g_code_start + g_code_first_layer + g_code_middle + g_code_end
print(g_code)

# hier wird der G-code abgespeichert
name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(g_code)
