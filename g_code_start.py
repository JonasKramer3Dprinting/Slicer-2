from g_code_functions import *

# hier wird der Start-code als Rückgabewert geliefert
def give_start_code(lh, bed_temperature, extruder_temperature):
    return (
        ";FLAVOR:Marlin \n;Layer height: "
        + str(lh)
        + " \n;Generated with Cura_SteamEngine 4.9.0 \n"
        + m140(bed_temperature-10)
        + "M105 \n"
        + m190(bed_temperature-10)
        + m140(bed_temperature)
        + m104(extruder_temperature)
        + "M105 \n"
        + m109(extruder_temperature)
        + m190(bed_temperature)
        + "M82 ;absolute extrusion mode \n; Ender 3 Custom Start G-code \nG92 E0 ; Reset Extruder \nG1 X0 Y0 Z10 F3000\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed \nG1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position \nG1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line \nG1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little \nG1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line \nG92 E0 ; Reset Extruder \nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed \nG1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish \nG92 E0 \nG92 E0 \nG1 F3000 E-8 \n"
    )
