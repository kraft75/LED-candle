"""
Aufgabe: Die Kerze 
 

Du besuchst ein Restaurant und siehst, dass sich unter der Tischdeko ein LED-Effekt verbirgt.
Fasziniert von diesem Farbwechsel stellst du fest, dass es sich hierbei um eine einzelne RGB handelt,
die erst blau leuchtet, dann langsam nach grün wechselt.
Nachdem das grüne Licht keine Blauanteile mehr enthält, passiert derselbe Effekt mit rot.
Das rote Licht geht wiederum in einen Blauton über. So lange die „LED-Kerze” eingeschaltet ist,
wiederholt sich dieser Effekt aufs Neue.  

Verwende für die folgenden Aufgaben die Tools uPyCraft, Fritzing und PAP-Designer. 
  
a Stelle dieses Dekorationselement in einer realen Situation nach. Erstelle den Stromlaufplan.  
b Überlege dir einen Weg, das Programm so effizient und strukturiert wie möglich aufzubauen.
  Verwende hierfür den PAP-Designer.  
c Programmiere den ESP32 so, dass das Programm ohne USB-Verbindung,
  zum Beispiel im Batterie- oder Solarbetrieb, funktionieren würde.   
"""

from machine import Pin, PWM
from time import sleep

""" Klasse Kerze """
class Kerze: 
    # Konstruktor 
    def __init__(self, pin1, pin2, pin3, freq):
        self.r = PWM(pin1, freq)
        self.g = PWM(pin2, freq)
        self.b = PWM(pin3, freq)        
            
    # Setzen der Ampelfarbe        
    def farbeSetzen(self, zahl1, zahl2, zahl3):
        self.r.duty(zahl1)
        self.g.duty(zahl2)
        self.b.duty(zahl3)
    
    
""" Hauptprogramm """
# Pins
r = Pin(12, Pin.OUT)
g = Pin(14, Pin.OUT)
b = Pin(27, Pin.OUT)

# Instanziierung Objekt Kerze
kerze = Kerze(r, g, b, 5000)
sleep(0.0001)
kerze.farbeSetzen(0, 0, 0)

# Zunehmende Farben
def farbeHoch(k, zahl):
    for i in range(255):
        # Rot nimmt zu
        if zahl == 1: 
            kerze.farbeSetzen(i, 0, 0)
            print(i)
            sleep(0.1)
        # Grün nimmt zu
        if zahl == 2: 
            kerze.farbeSetzen(0, i, 0)
            print(i)
            sleep(0.1)
        # Blau nimmt zu
        if zahl == 3: 
            kerze.farbeSetzen(0, 0, i)
            print(i)
            sleep(0.1)
            
# Abnehmende Farben            
def farbeRunter(k, zahl):
    for i in reversed(range(255)):
        # Rot nimmt ab
        if zahl == 1: 
            kerze.farbeSetzen(i, 0, 0)
            print(i)
            sleep(0.1)
        # Grün nimmt ab
        if zahl == 2: 
            kerze.farbeSetzen(0, i, 0)
            print(i)
            sleep(0.1)
        # Blau nimmt ab
        if zahl == 3: 
            kerze.farbeSetzen(0, 0, i)
            print(i)
            sleep(0.1)
    
    
sleep(1)

# Farbwechsel in Endlosschleife
counter = 0                                                    
while True:
    # Abnehmender Blauton
    farbeRunter(kerze, 3)
    # Ansteigender Grünton
    farbeHoch(kerze, 2)
    # Abnehmender Grünton
    farbeRunter(kerze, 2)
    # Ansteigender Rotton
    farbeHoch(kerze, 1)
    # Abnehmender Rotton
    farbeRunter(kerze, 1)
    # Ansteigender Blauton
    farbeHoch(kerze, 3)
    
    counter += 1
    """merken: 2 zählvariablen in Schleife for i, j in zip(range(255), reversed(range(255))):"""
    

