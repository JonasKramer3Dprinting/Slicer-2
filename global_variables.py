import math

pi = math.pi #Pi

# hier werden die globalen Variablen aufgelistet
tei = 0 # Extruder Temperatur erste Schicht
te = 0 # Extruder Temperatur
tbi = 0 # Bett Temperatur erste Schicht
tb = 0 # Bett Temperatur
lhi = 0 # Schichthöhe erste Schicht
lh = 0 # Schichthöhe
lwi = 0 # Linien Breite erste Schicht
lw = 0 # Linien Breite
fti = 0 # Bewegungsgeschwindigkeit erste Schicht
ft = 0 # Bewegungsgeschwindigkeit
fei = 0 # Extrusionsgeschwindigkeit erste Schicht
fe = 0 # Extrusionsgeschwindigkeit
rd = 0 # Einzugslänge

line_distance = 0 # Distanz die bei einer Bewegung überwunden wird
line_width = 0 # aktuelle Linienbreite
line_height = 0 # aktuelle Schichthöhe
travel_speed = 0 # aktuelle Bewegungsgeschwindigkeit
extrusion_speed = 0 # aktuelle Extrusionsgeschwindigkeit
extruder_temperature = 0 # aktuelle Extrudertemperatur
bed_temperature = 0 # aktuelle Betttemperatur
retraction_distance = 0 # aktuelle Einszugslänge

X = 0 # aktuelle x Koordinate
Y = 0 # aktuelle y Koordinate
Z = 0 # aktuelle z Koordinate
x = 0 # neue x Koordinate
y = 0 # neue y Koordinate 
z = 0 # neue z Koordinate
i = 0 # erste Koordinate Kreismittelpunkt
j = 0 # zweite Koordinate Kreismittelpunkt
r = 0 # Kreisradius

g_code_start = "" # Aufheizen + zwei Anfangslinien
g_code_first_layer = "" # erste Schicht
g_code_middle = "" # zweite bis letzte Schicht
g_code_end = "" # Druckende + Präsentation
g_code = "" # Gesamter G-code

option = 0 # Option, die gedruckt werden soll
placement = [] # die Positionierung des Objektes [x, y]
list = [] # die Liste mit den abzufahrenden Koordinaten [x0, y0, x1, y1, x2, y2, ...]
list_e = [] # die Liste mit der Information, ob bei einer Bewegung Material extrudiert werden soll, oder nicht [bool0, bool1, bool2, ...]
object_height = 0.0 # die Höhe des zu druckendem Objektes
