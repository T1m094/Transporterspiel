# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

import mainMenue

FPS = 60
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.joystick.init()

#TODO:

#    - Views:
#       - Hauptmenü <- ok
#       - Ergebnis WICHTIG ! 2h
#       - BevorGameStart <- muss einstellungen übergeben 1h
#       - Optionen  2h

#    - Festlegen der Parameter

#    - Lenkung nur Gas -> Joysick 30min
#    - Bug heli 30 min
#     - Tanken bei Zweispieler aus und selbst zurpück

#    - Bild LKW Voll halb leer 30 min

#    - Sound
#    - KM/H Anzeige <-?

#Erledigt:
#    - Tankanzeige
#    - Fahrzeuge nicht aus Spielfeld


    if pygame.joystick.get_count() != 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()


    pygame.display.set_caption("Transporterspiel")

    mainMenue.mainMenue()

    #spielLogik.spielStart()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
