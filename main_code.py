from global_variables import *

from g_code_functions import *

from print_settings import *

from option_quader import *

from option_extruded_polygon import *

from g_code_start import *

from g_code_end import *

option = print_options()

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

placement = placement_settings()

# hier wird die erste Option verwendet, falls dies zuvor angegeben wurde
if option == 0:
    list, list_e, object_height = optionZeroOne(line_width, placement[0], placement[1])
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

# hier wird die zweite Option verwendet, falls diese zuvor angegeben wurde

# hier wird der Code für die erste Schicht angefangen zu schreiben
z = line_height

# hier werden die gegebenen Punkte abgefahren

print(len(list), len(list), len(list_e), len(list_e))

g_code_first_layer = g0(list[0], list[1], z, travel_speed) + g1_retractreversed(
    8 - 8
)  # es wurden schon 8mm eingezogen und nun müssen wieder
for a in range(0, len(list) - 2, 2):
    x = list[a + 2]
    y = list[a + 3]
    if list_e[int(a / 2) + 1] == True:
        X = list[a]
        Y = list[a + 1]
        g_code_first_layer = g_code_first_layer + g1(
            x, y, z, extrusion_speed, X, Y, line_width, line_height, pi
        )
    else:
        g_code_first_layer = g_code_first_layer + g0(x, y, z, travel_speed)
g_code_first_layer = g_code_first_layer + g1_retract(retraction_distance)

(
    extruder_temperature,
    bed_temperature,
    line_height,
    line_width,
    travel_speed,
    extrusion_speed,
    retractionDistandance,
) = change_three(te, tb, lh, lw, ft, fe, rd)

# hier wird die erste Option verwendet, falls diese zuvor angegeben wurde
if option == 0:
    list, list_e, object_height = option_quader_two(line_width, placement[0], placement[1])
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

# hier wird die zweite Option verwendet, falls diese zuvor angegeben wurde

# hier wird der Code für die zweite Schicht angefangen zu schreiben
z = round((z + line_height), 6)
g_code_middle = m104(extruder_temperature) + m140(bed_temperature)

# hier werden die gegebenen Punkte abgefahren
for a in range(
    0, int(round((object_height - lhi) * 10 ** 12)) // int((line_height * 10 ** 12))
):

    g_code_middle = (
        g_code_middle
        + g0(list[0], list[1], z - line_height, travel_speed)
        + g0(
            list[0], list[1], z, travel_speed
        )  # Bewegung zum Ansatz wird bereits ausgeführt
        + g1_retractreversed(retraction_distance)
    )
    for a in range(0, len(list) - 2, 2):
        x = list[a + 2]
        y = list[a + 3]
        if (
            list_e[int(a / 2) + 1] == True
        ):  # der int ist um eine Einheit höher, siehe im letzten Kommentar
            X = list[a]
            Y = list[a + 1]
            g_code_middle = g_code_middle + g1(
                x, y, z, extrusion_speed, X, Y, line_width, line_height, pi
            )
        else:
            g_code_middle = g_code_middle + g0(x, y, z, travel_speed)
    g_code_middle = g_code_middle + g1_retract(retraction_distance)
    z = round((z + line_height), 6)

# mit folgendem Code wird der Endcode festgelegt
g_code_end = give_end_code()

# hier werdden die verschiedenen Codes addiert
gCode = g_code_start + g_code_first_layer + g_code_middle + g_code_end
print(gCode)

# hier wird der Code abgespeichert
name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(gCode)
