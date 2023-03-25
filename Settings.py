import pygame


#   Display
screen = pygame.display.set_mode()
pygame.font.init()
font = pygame.font.SysFont('Times', 15)


# Default Settings
#__________________
# Vehicle

# LKW
maxSpeedForward = 20    # Maximalgeschwindigkeit Vorwärts
maxSpeedBackward = 5    # Maximalgeschwindigkeit Rückwärts
speedUp = 0.5           # Beschleunigung
maxAngleSpeed = 2       # Wendekreis
maxLoadedQuantity = 20  # Maximale Ladekappazität Lkw

'''
# Hubschrauber
maxSpeedForward = 20    # Maximalgeschwindigkeit Vorwärts
maxSpeedBackward = 5    # Maximalgeschwindigkeit Rückwärts
speedUp = 0.5           # Beschleunigung
maxAngleSpeed = 2       # Wendekreis
maxLoadedQuantity = 20  # Maximale Ladekappazität Hubschrauber
'''

# DEBUGGER

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


