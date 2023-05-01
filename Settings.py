import pygame


#   Display
screen = pygame.display.set_mode()
pygame.font.init()
font = pygame.font.SysFont('Times', 15)
fontGuidText = pygame.font.SysFont('Times', 28)

# Settings
#__________________
# Vehicle

# Konfiguration des Schwierigkeitsgrads
# 0 - Leicht
# 1 - Mittel
# 2 - Schwer


#Schwellenwert für den Gewinn
thresholdToWin = 80

difficulty = 1

if difficulty == 0:

    # LKW:
    maxSpeedForwardTruck = 20
    maxSpeedBackwardTruck = 10
    speedUpTruck = 0.8
    maxAngleSpeedTruck = 3
    maxLoadedQuantityTruck = 15
    fuelConsumptionTruck = 0.1


    # Hubschrauber:
    maxSpeedForwardHeli = 15
    maxSpeedBackwardHeli = 3
    speedUpHeli = 0.5
    maxAngleSpeedHeli = 3
    maxLoadedQuantityHeli = 3
    fuelConsumptionHeli = 0.2


elif  difficulty == 1:

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


elif difficulty == 2:

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
# 0 - Tastatur
# 1 - Maus
# 2 - Joystick
# 3 - Folgen
controllerTruck = 1
controllerHeli = 4

# DEBUGGER
debugInfoColor = (0,255,0)
debug = False

debugPrints = False

def printDebugInfo(*args):
    if debugPrints:
        i = 0
        for array in args:
            for text_surface in array:
                screen.blit(text_surface, (20, i))
                i += 20
            i += 10


