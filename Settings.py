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

global difficulty
difficulty = 0
# Test Array
maxSpeedForwardTruck = [20, 15]
maxSpeedBackwardTruck = [10]
speedUpTruck = [1]
maxAngleSpeedTruck = [3]

maxLoadedQuantityTruck = [15]
fuelConsumptionTruck = [0.1]

# Hubschrauber:
maxSpeedForwardHeli = [15]
maxSpeedBackwardHeli = [3]
speedUpHeli = [0.5]
maxAngleSpeedHeli = [3]
maxLoadedQuantityHeli = [3]
fuelConsumptionHeli = [0.2]


# Steuerung für
# 0 - Tastatur
# 1 - Maus
# 2 - Joystick
# 3 - Folgen

global controllerTruck
global controllerHeli

controllerTruck = 0
controllerHeli = 3

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


