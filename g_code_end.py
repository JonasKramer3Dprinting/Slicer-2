from g_code_functions import *

def give_end_code():
    return "G91 ;Relative positioning\nG1 E-2 F2700 ;Retract a bit\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X5 Y5 F3000 ;Wipe out\nG1 Z10 ;Raise Z more\nG90 ;Absolute positioning\nG1 X0 Y220 ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\nM84 X Y Z E ;Disable all steppers\n;End of Gcode"
