import pygame


#   Display
screen = pygame.display.set_mode((1910, 1000))
pygame.font.init()
font = pygame.font.SysFont('Times', 15)


# Default Settings
#__________________
# Vehicle

# LKW
maxSpeedForward = 10    # Maximalgeschwindigkeit Vorwärts
maxSpeedBackward = 5    # Maximalgeschwindigkeit Rückwärts
speedUp = 0.5           # Beschleunigung
maxAngleSpeed = 2       # Wendekreis
maxLoadedQuantity = 20  # Maximale Ladekappazität Lkw
fuelConsumption = 0.1   # Sprit Verbrauch


# Hubschrauber
maxSpeedForwardHeli = 10   # Maximalgeschwindigkeit Vorwärts
maxSpeedBackwardHeli = 5    # Maximalgeschwindigkeit Rückwärts
speedUpHeli = 0.05        # Beschleunigung
maxAngleSpeedHeli = 2       # Wendekreis
maxLoadedQuantityHeli = 5  # Maximale Ladekappazität Hubschrauber
fuelConsumptionHeli = 0.1


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


