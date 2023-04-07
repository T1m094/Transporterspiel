# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

import spielLogik

FPS = 60
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.joystick.init()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    test = True


    pygame.display.set_caption("Transporterspiel")

    if test:
        spielLogik.spielStartTest()
    else:
        spielLogik.spielStart()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
