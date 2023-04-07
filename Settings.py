import pygame


#   Display
screen = pygame.display.set_mode()
pygame.font.init()
font = pygame.font.SysFont('Times', 15)


# Default Settings
#__________________
# Vehicle

# LKW
maxSpeedForwardTruck = 10    # Maximalgeschwindigkeit Vorwärts
maxSpeedBackwardTruck = 5    # Maximalgeschwindigkeit Rückwärts
speedUpTruck = 0.5           # Beschleunigung
maxAngleSpeedTruck = 2       # Wendekreis
maxLoadedQuantityTruck = 20  # Maximale Ladekappazität Lkw
fuelConsumptionTruck = 0.1   # Sprit Verbrauch

# Steuerung für
# 1 - Tastatur
# 2 - Maus
# 3 - Joystick
# 4 - Folgen

controllerTruck = 3# Default 1

# Hubschrauber
maxSpeedForwardHeli = 10   # Maximalgeschwindigkeit Vorwärts
maxSpeedBackwardHeli = 5    # Maximalgeschwindigkeit Rückwärts
speedUpHeli = 0.05        # Beschleunigung
maxAngleSpeedHeli = 2       # Wendekreis
maxLoadedQuantityHeli = 5  # Maximale Ladekappazität Hubschrauber
fuelConsumptionHeli = 0.1

controllerHeli = 4 # Default 4


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


