from global_variables import *

length = 0.0
width = 0.0
height = 0.0

# mit dieser Funktion wird die erste Obtion verwirklicht innerhalb der ersten Ebene

# mit der folgenden Funktion wird die Länge ermittelt und auch als Rückgabewert wiedergegeben
def option_quader_settings1():
    global length
    length = float(input("Give the length of the quader: "))
    return length

# mit der folgenden Funktion wird die Breite ermittelt und auch als Rückgabewert wiedergegeben
def option_quader_settings2():
    global width
    width = float(input("Give the width of the quader: "))
    return width

# mit der folgenden Funktion wird die Höhe ermittelt und auch als Rückgabewert wiedergegeben
def option_quader_settings3():
    global height
    height = float(input("Give the heigth of the quader: "))
    return height

# mit der folgenden Funktion wird die Liste, die Extrusionsliste und die Objekthöhe ermittelt
def option_quader(line_width, placement_x, placement_y, length, width, height):
    global list
    global list_e
    list = [] # Liste
    list_e = [] # Extrusionsliste
    local = 0 
    # mittel dieser IF-Verzweigung wird geprüft ob die eingegebene Länge oder Breite großer ist, da die Schicht in mittels immer kleiner werdender Rechtecke gedruckt wird, damit wird bei jedem Rechteck eine kleinere Breite und eine kleinere Länge genutzt, irgendwann wird jedoch die Länge oder Breite negativ, dann ist die Ebene fertig
    if length < width: 
        local = length
    else:
        local = width
    # Länge und Breite werden kopiert
    l = length
    w = width
    # local wird zu einem 10 ** 12 mal so großen int umgewandelt, um die Teilbarkeit mit Rest nutzen zu können 
    local = round(local * 10 ** 12, 0)
    local = int(local)
    print(height, local)
    # folgende Schleife generiert die Koordinaten für die Liste und die boolianischen Wert für die Extrusionsliste (die Schleife läuft, bis kein Rechteck mehr gedruckt werden kann)
    for a in range(0, local // int(line_width * 2 * 10 ** 12), 1):
        # diese zwei Koordinaten sind rechts oben
        list.append(w / 2 - line_width / 2)
        list.append(l / 2 - line_width / 2)
        # diese zwei Koordinaten sind links oben
        list.append(line_width / 2 - w / 2) 
        list.append(l / 2 - line_width / 2)
        # diese zwei Koordinaten sind links unten
        list.append(line_width / 2 - w / 2)
        list.append(line_width / 2 - l / 2)
        # diese zwei Koordinaten sind rechts unten
        list.append(w / 2 - line_width / 2) 
        list.append(line_width / 2 - l / 2)
        #diese zwei Koordinaten sind rechts oben
        list.append(w / 2 - line_width / 2)
        list.append(l / 2 - line_width / 2)
        #erst wird sich zum Ansatz bewegt, dabei soll kein Material extrudiert werden
        list_e.append(False) 
        #es werden 4 Linien abgefahren und dabei wird Material extrudiert, da die Extrusionslistenwert alle auf True gesetzt werden
        for a in range(0,4,1):
            list_e.append(True)
        # die kopierte Länge und Breite werden geringer, da beim nächsten durchlauf der Schleife Wert für ein kleineres Rechteck generiert werden sollen
        l = l - 2 * line_width
        w = w - 2 * line_width
        print(local)
        print(int(line_width * 2 * 10 ** 12))
        print(local % (int(line_width * 2 * 10 ** 12)))
    # bei dieser IF-Verzweigung wird geprüft, ob noch eine zusätzliche Linie in die ganzen Rechtecke hinein gedruckt werden kann
    if local % (int(line_width * 2 * 10 ** 12)) >= 10 ** 12:
        #hier ist diese letzte Linie horizontal
        if length > width:
            list.append(w / 2 - line_width / 2)
            list.append(l / 2 - line_width / 2)
            list.append(w / 2 - line_width / 2)
            list.append(line_width / 2 - l / 2)
        # hier ist diese letzte Linie vertikal
        else:
            list.append(w / 2 - line_width / 2)
            list.append(l / 2 - line_width / 2)
            list.append(line_width / 2 - w / 2)
            list.append(l / 2 - line_width / 2)
        # erst wird sich zum Ansatz bewegt
        list_e.append(False)
        # darauf wird eine letzte Linie gezogen
        list_e.append(True)
    print(list)
    print(list_e)
    #  es wird bei allen Koordinaten die Platzierung angefügt
    for a in range(0, len(list), 2):
        list[a] = round((list[a] + placement_x),6)
        list[a + 1] = round((list[a + 1] + placement_y),6)
    print(list)
    return list, list_e, height

# diese Funktion ruft die oben genannte Funktion auf und die Dimensionen des Quaders werden abgefragt
def option_quader_one(line_width, placement_x, placement_y):
    # es werden für die Funktion "optionZero()" benötigte Werte wiedergegeben und dabei können die Länge, Breite und Höhe eingegeben werden
    return option_quader(
        line_width,
        placement_x,
        placement_y,
        option_quader_settings1(),
        option_quader_settings2(),
        option_quader_settings3(),
    )

# diese Funktion ruft die oben genannte Funktion auf und es wird auf die bereits vorhandenen Dimensionen des Quaders zurückgegriffen
def option_quader_two(line_width, placement_x, placement_y):
     # es werden für die Funktion "option_quader()" benötigte Werte wiedergegeben und dabei werden die Länge, Breite und Höhe des Objektes vorausgesetzt, da diese im "mainCode" mittels der Methode "option_quader_one()", aus diesem Projekt, bereits ermittelt wurden
    return option_quader(line_width, placement_x, placement_y, length, width, height)