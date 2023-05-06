# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

import gameOverView
import mainMenue

FPS = 60
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.joystick.init()

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
