# hier wird die Funktion definiert, mit der die Druckeinstellungen gesetzt werden
def printSettings():
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
def changeOne(tei,tbi,lh):
    return tei,tbi,lh,10


# hier werden die Druckeinstellungen auf die Werte der ersten Ebene gesetzt
def changeTwo(tei,tbi,lhi,lwi,fti,fei,rd):
    return tei,tbi,lhi,lwi,fti,fei,rd


# hier werden die Druckeinstellungen auf die Werte der zweiten bis zur letzten Ebene gesetzt
def changeThree(te,tb,lh,lw,ft,fe,rd):
    return te,tb,lh,lw,ft,fe,rd