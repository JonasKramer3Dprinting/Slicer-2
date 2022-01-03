from global_variables import *

length = 0.0
width = 0.0
height = 0.0

# mit dieser Funktion wird die erste Obtion verwirklicht innerhalb der ersten Ebene

# mit den folgenden drei Funktionen werden die Länge, Breite und Höhe abgefragt und können eingegeben werden
def option_quader_settings1():
    global length
    length = float(input("Give the length of the quader: "))
    return length


def option_quader_settings2():
    global width
    width = float(input("Give the width of the quader: "))
    return width


def option_quader_settings3():
    global height
    height = float(input("Give the heigth of the quader: "))
    return height


def option_quader_one(line_width, placement_x, placement_y):
    return option_quader( # es werden für die Funktion "optionZero()" benötigte Werte wiedergegeben und dabei können die Länge, Breite und Höhe eingegeben werden
        line_width,
        placement_x,
        placement_y,
        option_quader_settings1(),
        option_quader_settings2(),
        option_quader_settings3(),
    )


def option_quader_two(line_width, placement_x, placement_y):
    return option_quader(line_width, placement_x, placement_y, length, width, height) # es werden für die Funktion "optionZero()" benötigte Werte wiedergegeben und dabei werden die Länge, Breite und Höhe des Objektes vorausgesetzt, da diese im "mainCode" mittels der Methode "optionZeroOne()", aus diesem Projekt, bereits ermittelt wurden


def option_quader(line_width, placement_x, placement_y, length, width, height):
    global list
    global list_e
    list = []
    list_e = []
    local = 0
    if length < width: # mittel dieser IF-Verzweigung wird geprüft ob die eingegebene Länge oder Breite großer ist, da die Schicht in mittels immer kleiner werdender Rechtecke gedruckt wird, damit wird bei jedem Rechteck eine kleinere Breite und eine kleinere Länge genutzt, irgendwann wird jedoch die Länge oder Breite negativ, dann ist die Ebene fertig
        local = length
    else:
        local = width
    l = length
    w = width
    local = round(local * 10 ** 12, 0)
    local = int(local)
    print(height, local)
    for a in range(0, local // int(line_width * 2 * 10 ** 12), 1): #die Schleif läuft, bis kein Rechteck mehr gedruckt werden kann
        list.append(w / 2 - line_width / 2) # diese zwei Koordinaten sind rechts oben
        list.append(l / 2 - line_width / 2)
        list.append(line_width / 2 - w / 2) # diese zwei Koordinaten sind links oben
        list.append(l / 2 - line_width / 2)
        list.append(line_width / 2 - w / 2) # diese zwei Koordinaten sind links unten
        list.append(line_width / 2 - l / 2)
        list.append(w / 2 - line_width / 2) # diese zwei Koordinaten sind rechts unten
        list.append(line_width / 2 - l / 2)
        list.append(w / 2 - line_width / 2) #diese zwei Koordinaten sind rechts oben
        list.append(l / 2 - line_width / 2)
        list_e.append(False) #erst wird sich zum Ansatz bewegt
        for a in range(0,4,1): #es werden 4 Linien abgefahren
            list_e.append(True)
        l = l - 2 * line_width
        w = w - 2 * line_width
        print(local)
        print(int(line_width * 2 * 10 ** 12))
        print(local % (int(line_width * 2 * 10 ** 12)))
    if local % (int(line_width * 2 * 10 ** 12)) >= 10 ** 12: # bei dieser IF-Verzweigung wird geprüft, ob noch eine zusätzliche Linie in die ganzen Rechtecke hinein gedruckt werden kann
        if length > width: #mit dieser IF-Verzweigung wird entschieden, ob diese zusätzliche Linie horizontal ist oder vertikal
            list.append(w / 2 - line_width / 2) #hier ist diese letzte Linie horizontal
            list.append(l / 2 - line_width / 2)
            list.append(w / 2 - line_width / 2)
            list.append(line_width / 2 - l / 2)
        else:
            list.append(w / 2 - line_width / 2) # hier ist diese letzte Linie vertikal
            list.append(l / 2 - line_width / 2)
            list.append(line_width / 2 - w / 2)
            list.append(l / 2 - line_width / 2)
        list_e.append(False) # erst wird sich zum Ansatz bewegt
        list_e.append(True) # es wird eine Linie gezogen
    print(list)
    print(list_e)
    for a in range(0, len(list), 2): # es wird bei allen Koordinaten die Platzierung angefügt
        list[a] = round((list[a] + placement_x),6)
        list[a + 1] = round((list[a + 1] + placement_y),6)
    print(list)
    return list, list_e, height
