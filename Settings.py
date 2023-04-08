import pygame


#   Display
screen = pygame.display.set_mode()
pygame.font.init()
font = pygame.font.SysFont('Times', 15)

# Settings
#__________________
# Vehicle

# Konfiguration des Schwierigkeitsgrads
# 1 - Leicht
# 2 - Mittel
# 3 - Schwer

difficulty = 2

if difficulty == 1:

    # LKW:
    maxSpeedForwardTruck = 10
    maxSpeedBackwardTruck = 3
    speedUpTruck = 0.03
    maxAngleSpeedTruck = 3
    maxLoadedQuantityTruck = 10
    fuelConsumptionTruck = 0.2


    # Hubschrauber:
    maxSpeedForwardHeli = 15
    maxSpeedBackwardHeli = 3
    speedUpHeli = 0.5
    maxAngleSpeedHeli = 3
    maxLoadedQuantityHeli = 3
    fuelConsumptionHeli = 0.2


elif  difficulty == 2:

    #LKW:
    maxSpeedForwardTruck = 15
    maxSpeedBackwardTruck = 5
    speedUpTruck = 0.04
    maxAngleSpeedTruck = 2
    maxLoadedQuantityTruck = 15
    fuelConsumptionTruck = 0.15

    #Hubschrauber:
    maxSpeedForwardHeli = 18
    maxSpeedBackwardHeli = 4
    speedUpHeli = 0.8
    maxAngleSpeedHeli = 2
    maxLoadedQuantityHeli = 4
    fuelConsumptionHeli = 0.15


elif difficulty == 3:

    # LKW:
    maxSpeedForwardTruck = 20
    maxSpeedBackwardTruck = 5
    speedUpTruck = 0.05
    maxAngleSpeedTruck = 1
    maxLoadedQuantityTruck = 20
    fuelConsumptionTruck = 0.1


    # Hubschrauber:
    maxSpeedForwardHeli = 20
    maxSpeedBackwardHeli = 5
    speedUpHeli = 1
    maxAngleSpeedHeli = 1
    maxLoadedQuantityHeli = 5
    fuelConsumptionHeli = 0.1


# Steuerung für
# 1 - Tastatur
# 2 - Maus
# 3 - Joystick
# 4 - Folgen
controllerTruck = 2
controllerHeli = 3





# DEBUGGER
debugInfoColor = (0,255,0)
debug = True

debugPrints = True


def printDebugInfo(*args):
    if debugPrints:
        i = 0
        for array in args:
            for text_surface in array:
                screen.blit(text_surface, (20, i))
                i += 20
            i += 10


